import datetime

from factory.fuzzy import FuzzyDate
from factory.django import DjangoModelFactory

from .models import Books


class BooksFactory(DjangoModelFactory):
    release_date = FuzzyDate(datetime.date.today())

    class Meta:
        model = Books
