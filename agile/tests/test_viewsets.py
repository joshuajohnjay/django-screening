import pytest

from django.urls import reverse

from typing import Dict

from rest_framework import status
from rest_framework.test import APIClient

from agile.models import Agile
from agile.tests.factory.user_factory import UserFactory
from agile.tests.factory.agile_factory import AgileFactory


@pytest.fixture
def agile_value() -> Agile:
    return AgileFactory.create(
        name="Individuals and interactions over processes and tools",
        description="This value of the Agile manifesto "
        + "focuses on giving importance",
    )


@pytest.fixture
def logged_in_client() -> APIClient:
    """Setup a fixture for an APIClient with a logged in user."""
    user = UserFactory()
    user.set_password("password")
    user.save()
    client = APIClient()
    client.login(username=user.username, password="password")  # nosec
    return client


@pytest.mark.django_db
class TestAgileViews:
    @pytest.fixture
    def defaults(self) -> Dict[str, Dict[str, str]]:
        payload = {
            "name": "Working product over comprehensive documentation",
            "description": "The Agile values dictate "
            + "that the first and foremost duty",
        }
        return {
            "payload": payload,
        }

    def get_detail_url(self, value_id):
        return reverse("agile:agile-detail", args=[value_id])

    def test_unauthenticated_list_view(self, client):
        """Tests get request are allowed for unauthenticated Users."""
        url = reverse("agile:agile-list")
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK  # nosec

    def test_list_view(self, logged_in_client):
        url = reverse("agile:agile-list")
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK  # nosec

    def test_get_view(self, logged_in_client, agile_value):
        url = self.get_detail_url(agile_value.id)
        resp = logged_in_client.get(url)
        assert resp.status_code == status.HTTP_200_OK  # nosec

    def test_unauthenticated_get_view(self, client, agile_value):
        """Tests get request are allowed for unauthenticated Users."""
        url = self.get_detail_url(agile_value.id)
        resp = client.get(url)
        assert resp.status_code == status.HTTP_200_OK  # nosec

    def test_unauthenticated_post(self, client, defaults):
        """Tests post request creates a Agile instance."""
        url = reverse("agile:agile-list")
        resp = client.post(url, defaults["payload"])
        assert resp.status_code == status.HTTP_403_FORBIDDEN  # nosec

    def test_post_type_value(self, logged_in_client, defaults):
        """Tests post request creates a Value instance."""
        url = reverse("agile:agile-list")
        paylod = defaults["payload"]
        paylod.update({"type": Agile.TYPE_VALUE})
        resp = logged_in_client.post(url, defaults["payload"])
        assert resp.status_code == status.HTTP_201_CREATED  # nosec
        agile = Agile.objects.get_or_none(id=resp.json()["id"])
        assert agile is not None  # nosec
        assert agile.type == Agile.TYPE_VALUE  # nosec

    def test_post_type_principle(self, logged_in_client, defaults):
        """Tests post request creates a Value instance."""
        url = reverse("agile:agile-list")
        paylod = defaults["payload"]
        paylod.update({"type": Agile.TYPE_PRINCIPLE})
        resp = logged_in_client.post(url, defaults["payload"])
        assert resp.status_code == status.HTTP_201_CREATED  # nosec
        agile = Agile.objects.get_or_none(id=resp.json()["id"])
        assert agile is not None  # nosec
        assert agile.type == Agile.TYPE_PRINCIPLE  # nosec

    def test_unauthenticated_patch(self, client, agile_value, defaults):
        """Tests post request creates a Agile instance."""
        url = self.get_detail_url(agile_value.id)
        resp = client.patch(url, defaults["payload"])
        assert resp.status_code == status.HTTP_403_FORBIDDEN  # nosec

    def test_patch(self, logged_in_client, agile_value):
        """Tests patch request updates the instance."""
        url = self.get_detail_url(agile_value.id)
        payload = {"description": "New Description"}
        resp = logged_in_client.patch(url, payload)
        assert resp.status_code == status.HTTP_200_OK  # nosec
        agile_value = Agile.objects.get(id=resp.json()["id"])
        assert agile_value.description == payload["description"]  # nosec

    def test_unauthenticated_put(self, client, agile_value, defaults):
        """Tests post request creates a Agile instance."""
        url = self.get_detail_url(agile_value.id)
        resp = client.put(url, defaults["payload"])
        assert resp.status_code == status.HTTP_403_FORBIDDEN  # nosec

    def test_put(self, logged_in_client, agile_value):
        """Tests put request updates an instance."""
        url = self.get_detail_url(agile_value.id)
        payload = {"name": "New Name", "description": "New Description"}
        resp = logged_in_client.put(url, payload)
        assert resp.status_code == status.HTTP_200_OK  # nosec
        agile_value = Agile.objects.get(id=resp.json()["id"])
        assert agile_value.description == payload["description"]  # nosec
        assert agile_value.name == payload["name"]  # nosec
