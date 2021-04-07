from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_password(self):
        with patch('requests.get') as i:
            i.return_value.text = "randompassword"
            response = self.client.get(url_for('password'))
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.data)

    def test_passwordstrength(self):
        with patch('requests.post') as g:
            g.return_value.text = "password"
            response = self.client.post(url_for('getPassStrength'), data = 'password')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'weak password', response.data)

            response2 = self.client.post(url_for('getPassStrength'), data = 'password123456789')
            self.assertEqual(response2.status_code, 200)
            self.assertIn(b'strong password', response2.data)