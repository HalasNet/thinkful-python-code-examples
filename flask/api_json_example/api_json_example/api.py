import json
from functools import wraps

from flask import request
from flask.ext.restful import reqparse, Api, Resource

from api_json_example import app



# Database?  We don't need no stinkin database
db = {}

api = Api(app)

def accept_json(func):
    """
    Decorator which returns a 406 Not Acceptable if the client won't accept JSON
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        accept = api.mediatypes()
        if "*/*" in accept or "application/json" in accept:
            return func(*args, **kwargs)
        return {"message": "Request must accept JSON"}, 406
    return wrapper

def require_json(func):
    """
    Decorator which returns a 415 Unsupported Media Type if the client sends
    something other than JSON
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.mimetype ==  "application/json":
            return func(*args, **kwargs)
        return {"message": "Request must contain JSON"}, 415
    return wrapper

class User(Resource):
    """
    A simple RESTful API for a user
    """
    parser = reqparse.RequestParser()

    method_decorators = [accept_json]

    def get(self, id):
        if not id in db:
            return {"message": "User not found"}, 404
        return db[id], 200

    @require_json
    def put(self, id):
        args = User.parser.parse_args()

        # Validate arguments
        if args["name"] and not isinstance(args["name"], basestring):
            return {"message": "Name must be a string"}, 422
        if args["email"] and not isinstance(args["email"], basestring):
            return {"message": "Email address must be a string"}, 422
        if (args["roles"] and
            not all(isinstance(role, basestring) for role in args["roles"])):
            return {"message": "Roles must be a strings"}, 422

        if id in db:
            # Edit user
            
            # SMELL: Merging could be nicer
            if args["name"]:
                db[id]["name"] = args["name"]
            if args["email"]:
                db[id]["email"] = args["email"]
            if args["roles"]:
                db[id]["roles"] = args["roles"]
            return db[id], 201, {"Location": "/api/user/{}".format(id)}
        else:
            # Create new user
            if not args["name"] or not args["email"]:
                return {"message": "Must provide name and email"}, 422

            db[id] = {
                "name": args["name"],
                "email": args["email"]
            }

            if args["roles"]:
                db[id]["roles"] = args["roles"]
            else:
                db[id]["roles"] = []

            return db[id], 200
        
User.parser.add_argument("name", type=str, location="get_json")
User.parser.add_argument("email", type=str, location="get_json")
User.parser.add_argument("roles", type=list, location="get_json")

api.add_resource(User, "/api/user/<int:id>")
