# Generated by Django 2.0.6 on 2018-06-16 17:47

from django.db import migrations, models
import mtg_deckbuilder.cards.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=256)),
                (
                    "colors",
                    mtg_deckbuilder.cards.models.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[("W", "White"), ("U", "Blue"), ("B", "Black"), ("R", "Red"), ("G", "Green")],
                            max_length=1,
                        ),
                        size=None,
                    ),
                ),
                (
                    "color_identity",
                    mtg_deckbuilder.cards.models.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[("W", "White"), ("U", "Blue"), ("B", "Black"), ("R", "Red"), ("G", "Green")],
                            max_length=1,
                        ),
                        size=None,
                    ),
                ),
                ("cmc", models.DecimalField(decimal_places=1, max_digits=4)),
                (
                    "card_types",
                    mtg_deckbuilder.cards.models.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("Basic", "Basic"),
                                ("Legendary", "Legendary"),
                                ("Ongoing", "Ongoing"),
                                ("Snow", "Snow"),
                                ("World", "World"),
                                ("Artifact", "Artifact"),
                                ("Conspiracy", "Conspiracy"),
                                ("Creature", "Creature"),
                                ("Enchantment", "Enchantment"),
                                ("Instant", "Instant"),
                                ("Land", "Land"),
                                ("Phenomenon", "Phenomenon"),
                                ("Plane", "Plane"),
                                ("Planeswalker", "Planeswalker"),
                                ("Scheme", "Scheme"),
                                ("Sorcery", "Sorcery"),
                                ("Tribal", "Tribal"),
                                ("Vanguard", "Vanguard"),
                            ],
                            max_length=16,
                        ),
                        size=None,
                    ),
                ),
                (
                    "sub_types",
                    mtg_deckbuilder.cards.models.ChoiceArrayField(
                        base_field=models.CharField(max_length=64), blank=True, size=None
                    ),
                ),
                ("uri", models.URLField()),
                ("scryfall_uri", models.URLField()),
            ],
        )
    ]
