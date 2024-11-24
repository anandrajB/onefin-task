import contextlib
from typing import Any, Dict, List, Union

from django.contrib.auth.models import User
from rest_framework import serializers

from utils.enum import ValidationEnum
from utils.typing import Movie as MovieDataType

from .models import Collections, Genre, Movies


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user_obj = User.objects.create_user(**validated_data)
        return user_obj


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collections
        fields = "__all__"

    def to_representation(self, instance: Collections):
        representation = super().to_representation(instance)
        with contextlib.suppress(Exception):
            if self.context.get("type_") == "get":
                [
                    representation.pop(key)
                    for key in ["created_at", "updated_at", "movies", "created_by"]
                ]
            else:
                [
                    representation.pop(key)
                    for key in ["created_at", "updated_at", "created_by", "uuid"]
                ]
        return representation


class MovieCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    genres = serializers.CharField(allow_blank=True)
    uuid = serializers.UUIDField()


class CollectionCreateUpdateSerializer(serializers.ModelSerializer):
    movies = MovieCreateSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Collections
        fields = "__all__"

    @staticmethod
    def validate_moviees_record(value: Any) -> List[Dict[str, str]]:
        base_errors = []
        for movie in value["movies"]:
            validation_errors = {}
            validation_rules = {
                "title": ValidationEnum.TITLE_REQUIRED,
                "description": ValidationEnum.MOVIE_REQUIRED,
                "genres": ValidationEnum.GENRE_REQUIRED,
            }
            for field, error_message in validation_rules.items():
                if not movie.get(field):
                    validation_errors[field] = error_message
            if validation_errors:
                base_errors.append(validation_errors)
        return base_errors

    @staticmethod
    def movie_and_genre_creation(
        movies_info_data: MovieDataType,
    ) -> Union[List[Movies], None]:
        if movies_info_data:
            movies_obj = []
            geners_obj = []
            for movie_info in movies_info_data:
                m_obj, _ = Movies.objects.get_or_create(
                    title=movie_info["title"],
                    defaults={
                        "description": movie_info["description"],
                    },
                )
                genre_names = movie_info.pop("genres")
                if not isinstance(genre_names, list):
                    genre_names = [name for name in genre_names.split(",")]
                for names in genre_names:
                    if names:
                        g_obj, _ = Genre.objects.get_or_create(name=names)
                        geners_obj.append(g_obj)
                        m_obj.genres.set(geners_obj)
                movies_obj.append(m_obj)
                m_obj.save()
            return movies_obj
        return None

    def run_validation(self, value) -> Union[serializers.ValidationError, Any]:
        errors = {}
        default_required_fields = ["title", "description", "movies"]
        for field in default_required_fields:
            if not value.get(field):
                errors[field] = f"the {field} field is required"
        if value.get("movies"):
            movie_record_errors = self.validate_moviees_record(value)
            if movie_record_errors:
                errors["movies"] = movie_record_errors
        if errors:
            raise serializers.ValidationError(errors)
        return value

    def create(self, validated_data: dict) -> "Collections":
        movies_validated_data = validated_data.pop("movies", [])
        added_movies = self.movie_and_genre_creation(movies_validated_data)
        collection_created_obj = Collections.objects.create(**validated_data)
        if added_movies:
            collection_created_obj.movies.set(added_movies)
        return collection_created_obj

    def update(self, instance: Collections, validated_data: dict):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        if validated_data.get("movies"):
            movies_validated_data = validated_data.get("movies")
            added_movies = self.movie_and_genre_creation(movies_validated_data)
            if added_movies:
                instance.movies.set(added_movies)
        instance.save()
        return instance
