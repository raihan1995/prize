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
        db.create_all()

        # Create test password
        sample1 = Password(password="abcdefghi12345")
        sample2 = Password(password="abcde12345")

        # Save password to password database
        db.session.add(sample1)
        db.session.commit()
        db.session.add(sample2)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    