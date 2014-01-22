import unittest
import json

import api_json_example

from api_json_example.api import db

class ApiTests(unittest.TestCase):
    def setUp(self):
        api_json_example.app.config.from_object("api_json_example.config.TestingConfig")
        self.client = api_json_example.app.test_client()

        db = {}

    def testPutCreateUser(self):
        response = self.client.put("/api/user/1",
            data=json.dumps({
                "name": "Joe Turner",
                "email": "joe@oampo.co.uk",
                "roles": ["admin", "user"]
            }),
            content_type="application/json",
            headers=[("Accept", "application/json")]
        )

        # Check the response status
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, "application/json")

        # Check the response data is correct
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Joe Turner")
        self.assertEqual(data["email"], "joe@oampo.co.uk")
        self.assertIn("admin", data["roles"])
        self.assertIn("user", data["roles"])

        # Check that it has been stored in the db correctly
        data = db[1]
        self.assertEqual(data["name"], "Joe Turner")
        self.assertEqual(data["email"], "joe@oampo.co.uk")
        self.assertIn("admin", data["roles"])
        self.assertIn("user", data["roles"])
        


    def testGetUser(self):
        db[1] = {
            "name": "Joe Turner",
            "email": "joe@oampo.co.uk",
            "roles": ["admin", "user"]
        }

        response = self.client.get("/api/user/1",
            headers=[("Accept", "application/json")]
        )

        # Check the response status
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        # Check the response data
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Joe Turner")
        self.assertEqual(data["email"], "joe@oampo.co.uk")
        self.assertIn("admin", data["roles"])
        self.assertIn("user", data["roles"])
        
