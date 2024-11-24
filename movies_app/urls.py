from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from movies_app.api.collection import (
    CollectionListCreateAPIView,
    CollectionRetriveUpdateAPIView,
)
from movies_app.api.movies import MoveisListApiView

from .views import UserRegiratrationAPIView

# ------------------------------------------------------------------------------------------

# BASE URL FOR ACCOUNTS

# -------------------------------------------------------------------------------------------


urlpatterns = [
    path("register", UserRegiratrationAPIView.as_view(), name="user-registration"),
    path("login", jwt_views.TokenObtainPairView.as_view(), name="token-obtrain-pair"),
    path("movies", MoveisListApiView.as_view(), name="movies-list"),
    path(
        "collection",
        CollectionListCreateAPIView.as_view(),
        name="collections-list-create",
    ),
    path(
        "collection/<str:pk>/",
        CollectionRetriveUpdateAPIView.as_view(),
        name="collection_view",
    ),
]
