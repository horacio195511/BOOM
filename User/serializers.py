from rest_framework import serializers
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = {
            'username', 'first_name', 'last_name', 'email'
        }
