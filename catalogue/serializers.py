#
# Serializers for use of REST API
# User -> superuser, active and admin
# Product
# Brand
#

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Brand

#Obtain model from auth
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.is_superuser = True
        user.is_staff = True
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "sku",
            "product_name",
            "product_price",
            "product_brand",
            "times_searched_anonymous"
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "brand_name",
            "pk",
        ]
