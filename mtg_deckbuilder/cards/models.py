from enum import Enum

from django import forms
from django.contrib.postgres.fields import ArrayField
from django.db import models


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.

    Usage:

        choices = ChoiceArrayField(models.CharField(max_length=...,
                                                    choices=(...,)),
                                   default=[...])
    """

    def formfield(self, **kwargs):
        kwargs.setdefault("form_class", forms.MultipleChoiceField)
        kwargs.setdefault("choices", self.base_field.choices)
        return super(ArrayField, self).formfield(**kwargs)  # pylint:disable=bad-super-call


def choices(enum):
    return [(v.value, v.name) for v in enum]


class CardType(Enum):
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


class Color(Enum):
    White = "W"
    Blue = "U"
    Black = "B"
    Red = "R"
    Green = "G"


# Create your models here.
class Card(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)
    colors = ChoiceArrayField(models.CharField(max_length=1, choices=choices(Color)))
    color_identity = ChoiceArrayField(models.CharField(max_length=1, choices=choices(Color)))
    cmc = models.DecimalField(max_digits=4, decimal_places=1)
    card_types = ChoiceArrayField(models.CharField(max_length=16, choices=choices(CardType)))
    sub_types = ChoiceArrayField(models.CharField(max_length=64), blank=True)
    uri = models.URLField()
    scryfall_uri = models.URLField()

    @classmethod
    def from_dict(cls, card):
        keys = {f.name for f in cls._meta.fields} - {"sub_types", "card_types"}

        types = [t.split() for t in card["type_line"].split("—")]
        if len(types) < 2:
            types += [[]]
        assert len(types) == 2, f"Error with parsing {card['type_line']!r}"
        card_types, sub_types = types
        assert card_types, f"Error when parsing {card['type_line']}"

        return cls.objects.create(**{key: card[key] for key in keys}, sub_types=sub_types, card_types=card_types)
