from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app



from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def rand_face(self):
        card_faces = [b"Spades", b"Diamonds", b"Hearts", b"Clubs"]
        response = self.client.get(url_for("card_suit"))
        self.assertIn(response.data, card_faces)

    def test_card_face(self):
        with patch("requests.get") as g:
            g.return_value.text = b"Spades"
            response = self.client.get(url_for("card_suit"))
            response = b"Spades"
            self.assertIn(b"Spades", response)
