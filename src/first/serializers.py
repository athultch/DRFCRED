# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):  # Corrected the class name

    class Meta:
        model = get_user_model()
        fields = "__all__"  # Remove the extra space

