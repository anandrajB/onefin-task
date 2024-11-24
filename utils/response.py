from rest_framework import status
from rest_framework.response import Response

from .enum import ResponseEnum


def SuccessResponse(data):
    return Response(
        {"status": ResponseEnum.SUCCESS, "data": data},
        status=status.HTTP_200_OK,
    )


def BadRequestResponse(data):
    return Response(
        {"status": ResponseEnum.FAILURE, "data": data},
        status=status.HTTP_400_BAD_REQUEST,
    )


def FailureResponse(data):
    return Response(
        {"status": ResponseEnum.FAILURE, "data": data},
        status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    )


def NotFoundResponse(data):
    return Response(
        {"status": ResponseEnum.NOT_FOUND, "data": data},
        status=status.HTTP_404_NOT_FOUND,
    )


def AcceptedReponse(data):
    return Response(
        {"status": ResponseEnum.ACCEPTED, "data": data},
        status=status.HTTP_202_ACCEPTED,
    )


def CreatedResponse(data):
    return Response(
        {"status": ResponseEnum.SUCCESS, "data": data}, status=status.HTTP_201_CREATED
    )
