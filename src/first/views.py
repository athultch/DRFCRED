
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer  # Use the corrected serializer class name

class UserViewSet(viewsets.ModelViewSet):  # Corrected the class name

    permission_classes = (IsAuthenticated,)  # Wrap IsAuthenticated in a tuple
    serializer_class = UserSerializer  # Use the corrected serializer class name
    queryset = get_user_model().objects.all()
