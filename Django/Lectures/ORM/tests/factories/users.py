import string

import factory
from factory import fuzzy

from apps.users.models import TrelloUser


class TrelloUserFactory(factory.django.DjangoModelFactory):
    first_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    last_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    username = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')

    class Meta:
        model = TrelloUser
