import os
from typing import Any, Union

import requests
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from utils.enum import ExceptionEnum, ResponseEnum
from utils.typing import MoviesResponse


class MoveisListApiView(APIView):
    permission_classes = [AllowAny]

    def __init__(self, *args, **kwargs):
        self.movies_url = os.environ.get("MOVIES_URL")
        self.username = os.environ.get("MOVIES_API_USERNAME")
        self.password = os.environ.get("MOVIES_API_PASSWORD")
        if not all([self.movies_url, self.username, self.password]):
            raise ValueError(ExceptionEnum.MISSING_CREDENTIALS.value)

    def get_movies_response(self) -> Union[MoviesResponse, Response]:
        page_number = self.request.query_params.get("page")
        base_url = (
            self.movies_url
            if not page_number
            else f"{self.movies_url}?page={page_number}"
        )
        absolute_uri = self.request.build_absolute_uri(reverse("movies-list"))
        try:
            movie_data: dict = requests.get(
                base_url, auth=(self.username, self.password), verify=False
            ).json()
            if movie_data.get("next"):
                movie_data["next"] = movie_data["next"].replace(base_url, absolute_uri)
            if movie_data.get("previous"):
                movie_data["previous"] = movie_data["previous"].replace(
                    base_url, absolute_uri
                )
            for movie in movie_data["results"]:
                if movie["genres"] is not None and len(movie["genres"]) > 0:
                    movie["genres"] = movie["genres"].split(",")
                else:
                    movie["genres"] = []
            return movie_data
        except requests.exceptions.RequestException as e:
            return Response(
                {ResponseEnum.ERROR: ExceptionEnum.CONNECTION_ERROR}, status=500
            )

    def get(self, request, *args: Any, **kwargs: Any) -> Response:
        movies_data = self.get_movies_response()
        return Response(movies_data if movies_data else None)
