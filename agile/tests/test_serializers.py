import pytest

from typing import Dict

from agile.models import Agile
from agile.serializers import AgileSerializer


@pytest.mark.django_db
class TestAgileSerializer:
    @pytest.fixture
    def agile_fixture(self, db) -> Agile:
        return Agile.objects.create(name="name", description="description")

    @pytest.fixture
    def defaults(self, agile_fixture) -> Dict[str, Dict[str, str]]:
        data = {
            "name": "Responding to change over following a plan.",
            "description": "Circumstances "
            + "change and sometimes customers demand extra.",
        }
        return {
            "page": agile_fixture,
            "data": data,
        }

    def test_valid(self, defaults):
        serializer = AgileSerializer(data=defaults["data"])
        assert serializer.is_valid() is True  # nosec

    def test_save(self, defaults):
        serializer = AgileSerializer(data=defaults["data"])
        serializer.is_valid()
        instance = serializer.save()
        assert instance.name == defaults["data"]["name"]  # nosec
        assert instance.description == defaults["data"]["description"]  # nosec
