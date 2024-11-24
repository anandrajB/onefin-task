import pytest
from django.utils import timezone

from movies_app.models import Collections, Genre, Movies


@pytest.mark.django_db
class TestGenreModel:
    def test_create_genre(self):
        genre = Genre.objects.create(name="Action")
        assert genre.name == "Action"


@pytest.mark.django_db
class TestMoviesModel:
    @pytest.fixture
    def genre(self):
        return Genre.objects.create(name="Action")

    def test_create_movie(self):
        movie = Movies.objects.create(
            title="Test Movie", description="Test Description"
        )
        assert movie.title == "Test Movie"
        assert movie.description == "Test Description"
        assert movie.created_at is not None
        assert movie.updated_at is not None

    def test_movie_with_genres(self, genre):
        movie = Movies.objects.create(
            title="Test Movie", description="Test Description"
        )
        movie.genres.add(genre)
        assert genre in movie.genres.all()

    def test_movie_str_method(self):
        movie = Movies.objects.create(
            title="Test Movie", description="Test Description"
        )
        assert movie.title == "Test Movie"

    def test_movie_uuid(self):
        movie = Movies.objects.create(
            title="Test Movie", description="Test Description"
        )
        assert movie.uuid is not None


@pytest.mark.django_db
class TestCollectionsModel:
    @pytest.fixture
    def user(self, django_user_model):
        return django_user_model.objects.create_user(
            username="testuser", password="testpass"
        )

    @pytest.fixture
    def movie(self):
        return Movies.objects.create(title="Test Movie", description="Test Description")

    def test_create_collection(self, user):
        collection = Collections.objects.create(
            title="My Collection",
            description="My Collection Description",
            created_by=user,
        )
        assert collection.title == "My Collection"
        assert collection.description == "My Collection Description"
        assert collection.created_by == user

    def test_collection_with_movies(self, user, movie):
        collection = Collections.objects.create(
            title="My Collection",
            description="My Collection Description",
            created_by=user,
        )

    def test_collection_without_title(self, user):
        collection = Collections.objects.create(
            description="No Title Collection", created_by=user
        )
        assert collection.title is None

    def test_collection_created_updated_at(self, user):
        collection = Collections.objects.create(
            title="My Collection",
            description="My Collection Description",
            created_by=user,
        )
        assert collection.created_at is not None
        assert collection.updated_at is not None
        assert isinstance(collection.created_at, timezone.datetime)
        assert isinstance(collection.updated_at, timezone.datetime)
