#
# REST Views for User, Product and Brand.
# GET
# POST
# UPDATE
# DELETE
#
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from .serializers import ProductSerializer, BrandSerializer, UserSerializer
from rest_framework.authtoken.admin import User


# User administration
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Product Administration

# Brand Administration
