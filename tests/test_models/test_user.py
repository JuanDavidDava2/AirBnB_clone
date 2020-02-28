#!/usr/bin/python3

""" Module to test User """


from models.user import User
import unittest
import models
import os


class TestUser(unittest.TestCase):
    """ Test of File Storage """

    def setUp(self):
        """SetUp method"""

        self.file_storage = User()

    def TearDown(self):
        """TearDown method."""

    del self.file_storage

    def test_doc(self):
        """Test docs for class"""

        self.assertIsNotNone(
            models.user.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(User.__doc__, "No docstring in the class")

    def test_permissions(self):
        """Test Permissions of file"""

        r = os.access('models/user.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/user.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/user.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.user.User'>")
        self.assertIsInstance(self.file_storage, User)
