from factory.django import DjangoModelFactory

from .models import Users


class UsersFactory(DjangoModelFactory):
    is_superuser = False
    is_staff = False

    class Meta:
        model = Users
