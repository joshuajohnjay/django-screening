import factory.fuzzy  # type: ignore

from agile.models import Agile


class AgileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Agile

    name = factory.Faker("name")
    type = factory.fuzzy.FuzzyChoice([x[0] for x in Agile.AGILE_TYPES_CHOICES])
