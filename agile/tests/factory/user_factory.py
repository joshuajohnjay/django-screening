import factory.fuzzy  # type: ignore

from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
