#!/usr/bin/python3

""" Module to test Review """


from models.review import Review
import unittest
import models
import os


class TestReview(unittest.TestCase):
    """ Test of File Storage """

    def setUp(self):
        """SetUp method"""

        self.file_storage = Review()

    def TearDown(self):
        """TearDown method."""

        del self.file_storage

    def test_doc(self):
        """Test docs for class"""

        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the class")

    def test_permissions(self):
        """Test Permissions of file"""

        r = os.access('models/review.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/review.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/review.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(self.file_storage, Review)
