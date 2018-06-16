# Create your tests here.

from hypothesis.extra import django

from .models import Card


class TestCard(django.TestCase):
    def test_card_from_dict(self):
        card_dict = {
            "id": "8bcfd255-7ee7-409e-9a1e-ec5bcabce075",
            "name": "card",
            "colors": ["U"],
            "color_identity": ["U"],
            "cmc": "1.0",
            "type_line": "Creature - Archer",
            "scryfall_uri": "https://url.com",
            "uri": "https://url.com",
        }
        Card.from_dict(card_dict)
