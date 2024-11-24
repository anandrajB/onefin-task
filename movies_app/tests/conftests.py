import pytest
from django.contrib.auth.models import User

from movies_app.models import Collections, Genre, Movies


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", password="testpassword", email="test@example.com"
    )


@pytest.fixture
def genre(db):
    return Genre.objects.create(name="Action")


@pytest.fixture
def movie(db):
    return Movies.objects.create(title="Test Movie", description="Test Description")


@pytest.fixture
def collection(db, user):
    return Collections.objects.create(
        title="Test Collection",
        description="Test Collection Description",
        created_by=user,
    )


@pytest.fixture
def client_with_user(client, user):
    client.login(username="testuser", password="testpassword")
    return client
