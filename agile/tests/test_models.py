from django.test import TestCase

from agile.models import Agile


class AgileMethodTests(TestCase):
    def test_get_values(self):
        """Tests expected Agile type values from fixtures."""
        self.assertTrue(Agile.objects.get_values().count(), 4)

    def test_get_principles(self):
        """Tests expected Agile type principles from fixtures."""
        self.assertTrue(Agile.objects.get_principles().count(), 12)

    def test_get_or_none_found(self):
        """Tests expected Agile instance."""
        self.assertIsInstance(Agile.objects.get_or_none(id=1), Agile)

    def test_get_or_none(self):
        """Tests expects none."""
        self.assertIsNone(Agile.objects.get_or_none(id=20))

    def test_uuid_present(self):
        """Tests expects none."""
        agile = Agile.objects.all()
        for a in agile:
            assert a.uuid is not None  # nosec
