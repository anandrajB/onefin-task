import datetime
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from django.http import JsonResponse
from django.core.cache import cache

logger = logging.getLogger(__name__)
def index(request):
    logger.info("Homepage was accessed at " + str(datetime.datetime.now()) + " hours!")
    return JsonResponse({"hello": "world"})


def request_count(request):
    logger.info("new request count added at" + str(datetime.datetime.now()) + " hours!")
    return JsonResponse({"requests": cache.get("request_count")})


def request_count_reset(request):
    cache.delete("request_count")
    logger.warning("request count reset at " + str(datetime.datetime.now()) + " hours!")
    return JsonResponse({"message": "request count reset successfully"})


class UserRegiratrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"access_token": str(AccessToken().for_user(user))})
