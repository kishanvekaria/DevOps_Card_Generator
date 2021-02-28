from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def rand_face(self):
        card_faces = [b"Ace", b"King", b"Queen", b"Jack"]
        response = self.client.get(url_for("card_number"))
        self.assertIn(response.data, card_faces)

    def test_card_face(self):
        with patch("requests.get") as g:
            g.return_value.text = b"King"
            response = self.client.get(url_for("card_number"))
            response = b"King"
            self.assertIn(b"King", response)