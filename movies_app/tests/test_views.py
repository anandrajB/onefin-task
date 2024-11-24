import os
import pytest
import requests
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
@patch("requests.get")
def test_get_movies_success(mock_get, client):
    mock_get.return_value.json.return_value = {
        "results": [{"id": 1, "title": "Inception", "genres": "Sci-Fi,Thriller"}],
        "next": None,
        "previous": None,
    }
    response = client.get(reverse("movies-list"))
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data["results"][0]["genres"] == ["Sci-Fi", "Thriller"]


@pytest.mark.django_db
@patch("requests.get")
def test_get_movies_connection_error(mock_get, client):
    mock_get.side_effect = requests.exceptions.RequestException
    response = client.get(reverse("movies-list"))
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.data == {"error": "Connection error"}
