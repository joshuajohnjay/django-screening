import pytest

from agile.models import Agile


@pytest.fixture
def agile() -> Agile:
    return Agile.objects


@pytest.mark.django_db
class TestAgileMethod:
    def test_get_values(self, agile):
        """Tests expected Agile type values from fixtures."""
        assert agile.get_values().count() == 4  # nosec

    def test_get_principles(self, agile):
        """Tests expected Agile type principles from fixtures."""
        assert agile.get_principles().count() == 12  # nosec

    def test_get_or_none_found(self, agile):
        """Tests expected Agile instance."""
        assert isinstance(agile.get_or_none(id=1), Agile)  # nosec

    def test_get_or_none(self, agile):
        """Tests expects none."""
        assert agile.get_or_none(id=20) is None  # nosec
