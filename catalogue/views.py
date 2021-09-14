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
from .models import Product, Brand


# User administration
class CreateUserView(CreateAPIView):
    """
        List all users, or create a new user.
    """
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Product Administration
class ProductList(generics.ListCreateAPIView):
    """
        List all products, or create a new product.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
       Retrieve, update or delete a product instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        if not request.user.is_authenticated:
            data2 = {'times_searched_anonymous': product.times_searched_anonymous + 1}
            serializer2 = ProductSerializer(product, data=data2, partial=True)
            if serializer2.is_valid():
                serializer2.save()
                return Response(serializer2.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Brand Administration
class BrandList(generics.ListCreateAPIView):
    """
        List all brands, or create a new brand.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    """
       Retrieve, update or delete a brand instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
