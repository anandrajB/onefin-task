import uuid

from django.contrib.auth.models import User
from django.db import models


def hex_uuid():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=hex_uuid, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Movies(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="movies_genres", blank=True)

    def __str__(self) -> str:
        return self.title


class Collections(BaseModel):
    title = models.CharField(max_length=555, blank=True, null=True)
    description = models.TextField()
    movies = models.ManyToManyField(
        Movies, related_name="movie_collections", blank=True
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.title
