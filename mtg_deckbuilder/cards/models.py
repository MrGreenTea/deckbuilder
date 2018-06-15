import enum

from django.contrib.postgres import fields
from django.db import models


class CardType(enum.Enum):
    Artifact = 'Artifact'
    Conspiracy = 'Conspiracy'
    Creature = 'Creature'
    Enchantment = 'Enchantment'
    Instant = 'Instant'
    Land = 'Land'
    Phenomenon = 'Phenomenon'
    Plane = 'Plane'
    Planeswalker = 'Planeswalker'
    Scheme = 'Scheme'
    Sorcery = 'Sorcery'
    Tribal = 'Tribal'
    Vanguard = 'Vanguard'

    @classmethod
    def choices(cls):
        return [(v.value, v.name) for v in cls]


class SuperType(enum.Enum):
    Basic = 'Basic'
    Legendary = 'Legendary'
    Ongoing = 'Ongoing'
    Snow = 'Snow'
    World = 'World'

    @classmethod
    def choices(cls):
        return [(v.value, v.name) for v in cls]


# Create your models here.
class Card(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)
    cmc = models.DecimalField(max_digits=4, decimal_places=1)
    super_types = fields.ArrayField(models.CharField(max_length=16, choices=SuperType.choices()))
    card_types = fields.ArrayField(models.CharField(max_length=16, choices=CardType.choices()))
    sub_types = fields.ArrayField(models.CharField(max_length=64))
    uri = models.URLField()
    scryfall_uri = models.URLField()
