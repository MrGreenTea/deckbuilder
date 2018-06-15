import enum

from django.contrib.postgres import fields
from django.db import models


class CardType(enum.Enum):
    Basic = "Basic"
    Legendary = "Legendary"
    Ongoing = "Ongoing"
    Snow = "Snow"
    World = "World"
    Artifact = "Artifact"
    Conspiracy = "Conspiracy"
    Creature = "Creature"
    Enchantment = "Enchantment"
    Instant = "Instant"
    Land = "Land"
    Phenomenon = "Phenomenon"
    Plane = "Plane"
    Planeswalker = "Planeswalker"
    Scheme = "Scheme"
    Sorcery = "Sorcery"
    Tribal = "Tribal"
    Vanguard = "Vanguard"

    @classmethod
    def choices(cls):
        return [(v.value, v) for v in cls]


class Color(enum.Enum):
    White = "W"
    Blue = "U"
    Black = "B"
    Red = "R"
    Green = "G"

    @classmethod
    def choices(cls):
        return [(v.value, v) for v in cls]


# Create your models here.
class Card(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)
    colors = fields.ArrayField(models.CharField(max_length=1, choices=Color.choices()))
    color_identity = fields.ArrayField(models.CharField(max_length=1, choices=Color.choices()))
    cmc = models.DecimalField(max_digits=4, decimal_places=1)
    card_types = fields.ArrayField(models.CharField(max_length=16, choices=CardType.choices()))
    sub_types = fields.ArrayField(models.CharField(max_length=64), blank=True)
    uri = models.URLField()
    scryfall_uri = models.URLField()

    @classmethod
    def from_dict(cls, card):
        scry_id = card["id"]
        name = card["name"]
        cmc = card["cmc"]
        uri = card["uri"]
        scryfall_uri = card["scryfall_uri"]

        types = [t.split() for t in card["type_line"].split("—")]
        if len(types) < 2:
            types += []
        assert len(types) == 2, f'Error with parsing {card["type_line"]!r}'
        card_types, sub_types = types
        assert card_types, f'Error when parsing {card["type_line"]}'

        return cls(
            id=scry_id,
            name=name,
            cmc=cmc,
            uri=uri,
            scryfall_uri=scryfall_uri,
            sub_types=sub_types,
            card_types=card_types,
        )
