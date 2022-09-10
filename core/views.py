from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from .contrib.unique_none import get_unique_or_none
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from rest_framework import status


class LoginView(APIView):
    """Api view for user login & current logged in user.
    """

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        """Get logged in user.
        """
        if type(request.user) != AnonymousUser:
            user = get_unique_or_none(User, id=request.user.id)
            serializer = UserSerializer(user)

            return Response(serializer.data)
        return Response({})

    def post(self, request):
        try:
            """User login
            """
            user_name = request.data.get('username')
            password = request.data.get('password')

            user = get_unique_or_none(User, username=user_name)
            if not user:
                raise AuthenticationFailed(f'User "{user_name}" not found.')

            user = authenticate(username=user_name, password=password)

            if user is None:
                raise AuthenticationFailed(
                    f'Login failed for user "{user_name}."'
                )

            login(request, user)
            user = get_unique_or_none(User, pk=request.user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        except Exception as e:
            return Response(
                data={'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class LogoutView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def post(self, request):
        """Logout the user.
        """
        try:
            logout(request)
            return Response(data={'message': 'Logged out.'})
        except Exception:
            return Response(data={'message': 'Logout failed.'})
