#!/usr/bin/python3

""" Module to test FileStorage """


from models.engine.file_storage import FileStorage
import unittest
import models
import os


class TestFileStorage(unittest.TestCase):
    """ Test of File Storage """

    def setUp(self):
        """SetUp method"""

        self.file_storage = FileStorage()

    def TearDown(self):
        """TearDown method."""

        del self.file_storage

    def test_doc(self):
        """Test docs for class"""

        self.assertIsNotNone(
            models.engine.file_storage.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(FileStorage.__doc__, "No docstring in the class")

    def test_permissions(self):
        """Test Permissions of file"""

        r = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(self.file_storage, FileStorage)
