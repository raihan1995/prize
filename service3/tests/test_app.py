from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_letters(self):
        response = self.client.get(url_for('digits'))
        self.assertEqual(response.status_code, 200)
    
    def test_get_letters(self):
        response = self.client.get(url_for('digits'))
        self.assertIsNotNone(response.data)
    