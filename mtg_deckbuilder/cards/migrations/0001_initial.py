# Generated by Django 2.0.6 on 2018-06-13 12:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('cmc', models.DecimalField(decimal_places=1, max_digits=4)),
                ('super_types', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(choices=[(1, 'Basic'), (2, 'Legendary'), (3, 'Ongoing'), (4, 'Snow'), (5, 'World')]), size=None)),
                ('card_types', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(choices=[(1, 'Artifact'), (2, 'Conspiracy'), (3, 'Creature'), (4, 'Enchantment'), (5, 'Instant'), (6, 'Land'), (7, 'Phenomenon'), (8, 'Plane'), (9, 'Planeswalker'), (10, 'Scheme'), (11, 'Sorcery'), (12, 'Tribal'), (13, 'Vanguard')]), size=None)),
                ('sub_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('uri', models.URLField()),
                ('scryfall_uri', models.URLField()),
            ],
        ),
    ]