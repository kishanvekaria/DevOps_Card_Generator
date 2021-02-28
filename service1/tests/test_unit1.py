from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase
from os import getenv
from app import app, Storage

class TestBase(TestCase):
    def create_app(self):
        return app
    

class TestResponse(TestBase):
    def test_card_face_page(self):
        with patch("requests.get") as g:
            g.return_value.text = "King"
            response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'King', response.data)

        