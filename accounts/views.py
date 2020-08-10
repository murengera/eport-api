from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from accounts.serializer import UserSerializer, LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CreateUserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer




class Loginview(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data("user")
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class Logoutview(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        django_logout(request)
        return Response(status=204)


