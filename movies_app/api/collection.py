from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from movies_app.models import Collections
from movies_app.serializers import (
    CollectionCreateUpdateSerializer,
    CollectionSerializer,
)
from utils.enum import ResponseEnum
from utils.response import (
    AcceptedReponse,
    BadRequestResponse,
    NotFoundResponse,
    SuccessResponse,
)


class CollectionListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionCreateUpdateSerializer

    def list(self, request) -> Response:
        collection_queryst = Collections.objects.filter(created_by=request.user)
        serializer = CollectionSerializer(
            collection_queryst, many=True, context={"type_": "get"}
        )
        if collection_queryst:
            return Response(
                {
                    "is_success": True,
                    "data": {
                        "collections": serializer.data,
                        "favourite_genres": collection_queryst.values_list(
                            "movies__genres__name", flat=True
                        )[:3],
                    },
                }
            )
        return SuccessResponse(serializer.data)

    def create(self, request) -> Response:
        serializer = CollectionCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(
                {"collection_uuid": serializer.data["uuid"]},
                status=status.HTTP_201_CREATED,
            )
        return BadRequestResponse(serializer.errors)


class CollectionRetriveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionCreateUpdateSerializer

    def get_queryset(self, request: Request, *args, **kwargs) -> QuerySet:
        return get_object_or_404(
            Collections, uuid=self.kwargs["pk"], created_by=request.user
        )

    def retrieve(self, request, pk: str) -> Response:
        try:
            serializer = CollectionSerializer(
                self.get_queryset(request, pk),
                context={"type_": "retrieve"},
            )
            return SuccessResponse(serializer.data)
        except Collections.DoesNotExist:
            return NotFoundResponse(ResponseEnum.COLLECTION_NOT_FOUND)

    def update(self, request, pk: str) -> Response:
        try:
            serializer = CollectionCreateUpdateSerializer(
                self.get_queryset(request, pk), data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return AcceptedReponse(ResponseEnum.RECORD_UPDATED)
            return BadRequestResponse(serializer.errors)
        except Collections.DoesNotExist:
            return NotFoundResponse(ResponseEnum.COLLECTION_NOT_FOUND)

    def delete(self, request, pk: str) -> Response:
        try:
            collection_obj = self.get_queryset(request, pk)
            collection_obj.delete()
            return SuccessResponse(ResponseEnum.RECORD_DELETED)
        except Collections.DoesNotExist:
            return NotFoundResponse(ResponseEnum.COLLECTION_NOT_FOUND)
