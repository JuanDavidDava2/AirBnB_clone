#!/usr/bin/python3

""" Module to test BaseModel """


from models.base_model import BaseModel
import unittest
import models
import os


class TestBaseModel(unittest.TestCase):
    """ Test of File Storage """

    def setUp(self):
        """SetUp method"""

        self.file_storage = BaseModel()

    def TearDown(self):
        """TearDown method."""

        del self.file_storage

    def test_doc(self):
        """Test docs for class"""

        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def test_permissions(self):
        """Test Permissions of file"""

        r = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.file_storage, BaseModel)
