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
        sample1 = Password(password="pasword12334567890")
        sample2 = Password(password="password")

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
        with patch('requests.get') as g:
            g.return_value.text = "randompassword"
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.data)

    # def test_passwordstrength(self):
    #     with patch('requests.post') as g:
    #         g.return_value.text = "password"
    #         response = self.client.post(url_for('getPassStrength'), data = 'password')
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b'weak password', response.data)

    #         response2 = self.client.post(url_for('getPassStrength'), data = 'password123456789')
    #         self.assertEqual(response2.status_code, 200)
    #         self.assertIn(b'strong password', response2.data)

# class TestResponse(TestBase):

#     def test_home_get(self):
#         response = self.client.get(url_for('home'))
#         self.assertEqual(response.status_code, 200)

    # def test_spirit_on_page(self):
    #     with patch("requests.get") as g:
    #             with patch("requests.post") as p:
    #                 g.return_value.text = "Vodka"
    #                 p.return_value.text = "Orange Juice"

    #                 response = self.client.get(url_for("index"))
    #                 self.assertEqual(response.status_code, 200)
    #                 self.assertIn(b'Have a <b>Vodka</b> with <b>Orange Juice</b>', response.data)
    