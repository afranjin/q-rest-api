from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    user_fullname = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'
