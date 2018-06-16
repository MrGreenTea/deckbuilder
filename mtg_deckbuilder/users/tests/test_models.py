from hypothesis import given
from hypothesis.extra.django import TestCase, models

from ..models import User


class TestUser(TestCase):
    @given(models.models(User))
    def test_get_absolute_url(self, user):
        user.get_absolute_url()
