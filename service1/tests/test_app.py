from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
from app import app, db, Password

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        # Create table
        db.drop_all()
        db.create_all()

        # Create test password
        pass1 = Password(password="pasword12334567890")
        pass2 = Password(password="password")

        # Save password to password database
        db.session.add(pass1)
        db.session.commit()
        db.session.add(pass2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        with patch('requests.get') as g:
            with patch('requests.post') as i:
                g.return_value.text = "randompassword"
                i.return_value.text = "password"
                response = self.client.get(url_for('home'))
                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(response.data)