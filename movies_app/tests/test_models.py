import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from movies_app.models import Genre, Collections, Movies


@pytest.mark.django_db
class TestGenreModel:
    def test_create_genre(self):
        genre = Genre.objects.create(name="Action")
        assert genre.name == "Action"
        assert str(genre) == "Action"

    def test_unique_genre_name(self, genre):
        with pytest.raises(ValidationError):
            Genre.objects.create(name="Action")


@pytest.mark.django_db
class TestMoviesModel:
    def test_create_movie(self):
        movie = Movies.objects.create(
            title="Test Movie", description="Test Description"
        )
        assert movie.title == "Test Movie"
        assert movie.description == "Test Description"
        assert movie.created_at is not None
        assert movie.updated_at is not None

    def test_movie_with_genres(self, movie, genre):
        movie.genres.add(genre)
        assert genre in movie.genres.all()

    def test_movie_str_method(self, movie):
        assert str(movie) == "Test Movie"

    def test_movie_uuid(self, movie):
        assert movie.uuid is not None


@pytest.mark.django_db
class TestCollectionsModel:
    def test_create_collection(self, user):
        collection = Collections.objects.create(
            title="My Collection",
            description="My Collection Description",
            created_by=user,
        )
        assert collection.title == "My Collection"
        assert collection.description == "My Collection Description"
        assert collection.created_by == user

    def test_collection_with_movies(self, collection, movie):
        collection.movies.add(movie)
        assert movie in collection.movies.all()

    def test_collection_without_title(self, user):
        collection = Collections.objects.create(
            description="No Title Collection", created_by=user
        )
        assert collection.title is None

    def test_collection_created_updated_at(self, collection):
        assert collection.created_at is not None
        assert collection.updated_at is not None
        assert isinstance(collection.created_at, timezone.datetime)
        assert isinstance(collection.updated_at, timezone.datetime)

    def test_collection_str_method(self, collection):
        assert str(collection) == "Test Collection"
