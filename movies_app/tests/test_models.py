import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from movies_app.tests.factories import GenreFactory, MovieFactory, CollectionFactory


@pytest.mark.django_db
class TestGenreModel:
    def test_create_genre(self):
        genre = GenreFactory(name="Action")
        assert genre.name == "Action"
        assert str(genre) == "Action"

    def test_unique_genre_name(self):
        GenreFactory(name="Action")
        with pytest.raises(ValidationError):
            GenreFactory(name="Action")


@pytest.mark.django_db
class TestMoviesModel:
    def test_create_movie(self):
        movie = MovieFactory()
        assert movie.title is not None
        assert movie.description is not None
        assert movie.created_at is not None
        assert movie.updated_at is not None

    def test_movie_with_genres(self):
        genre = GenreFactory()
        movie = MovieFactory()
        movie.genres.add(genre)
        assert genre in movie.genres.all()

    def test_movie_str_method(self):
        movie = MovieFactory(title="Test Movie")
        assert str(movie) == "Test Movie"

    def test_movie_uuid(self):
        movie = MovieFactory()
        assert movie.uuid is not None


@pytest.mark.django_db
class TestCollectionsModel:
    @pytest.fixture
    def user(self, django_user_model):
        return django_user_model.objects.create_user(
            username="testuser", password="testpass"
        )

    def test_create_collection(self, user):
        collection = CollectionFactory(created_by=user)
        assert collection.title is not None
        assert collection.description is not None
        assert collection.created_by == user

    def test_collection_with_movies(self, user):
        collection = CollectionFactory(created_by=user)
        movie = MovieFactory()
        collection.movies.add(movie)
        assert movie in collection.movies.all()

    def test_collection_without_title(self, user):
        collection = CollectionFactory(title=None, created_by=user)
        assert collection.title is None

    def test_collection_created_updated_at(self, user):
        collection = CollectionFactory(created_by=user)
        assert collection.created_at is not None
        assert collection.updated_at is not None
        assert isinstance(collection.created_at, timezone.datetime)
        assert isinstance(collection.updated_at, timezone.datetime)
