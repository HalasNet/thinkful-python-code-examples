# Making a Flask extension which creates SQLAlchemy models

**Warning** If you're eating your breakfast, look away now - this technique is full of ugly

The codebase:

- __init__.py - An example app.  Creates an instance of our model.
- models.py - Contains database and extension initialization, as well as our model.
- sqla/__init__.py - A mock object which looks a little bit like the Flask-SQLAlchemy module.  Used because I'm too lazy to set up a virtualenv.
- flask_permissions/__init__.py - The extension we are writing.  Provides some models which can be created or extended, and stored in the database.
- flask_permissions/permissions.py - Provides the extension object.
- flask_permissions/models.py - The models which we want to supply.

The trick:

We have to have access to an instantiated db object in order to create the models for our extension, but we don't know what it's called, or where it lives.  So how do we access it, and create the models?

1. We make the user pass the db object in to an init method when they create an instance of our extension object.
2. Inside the init method, we create a new global variable called db.
3. When we create the models we try to import the db global.
4. If the import fails we throw an error saying that the user needs to initialize the extension object before importing the models.

The use of globals, plus the fact that the import only works when you put it in the right place are gigantic signposts that this is not pretty.  But then again, having to derive classes from `instance.Class` is also fairly horrible, so hold your nose and fill yer boots.

