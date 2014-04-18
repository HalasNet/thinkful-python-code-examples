import unittest
import os

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "app.config.TestingConfig"

from app import app
from app import models
from app.database import Base, engine, session

class Test(unittest.TestCase):
    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

