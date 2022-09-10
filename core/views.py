from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from .contrib.unique_none import get_unique_or_none
from .serializers import UserSerializer
from rest_framework.response import Response


class LoginView(APIView):
    """Api view for login/logout/current logged in user.
    """

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        """Logged in user.
        """
        if type(request.user) != AnonymousUser:
            user = get_unique_or_none(User, id=request.user.id)
            serializer = UserSerializer(user)

            return Response(serializer.data)
        return Response({})
