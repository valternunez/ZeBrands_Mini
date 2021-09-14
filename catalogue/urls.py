#
# URL management file for REST API
#

from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductList.as_view()),
    path("product/<int:pk>", views.ProductDetail.as_view()),
    path("brand/", views.BrandList.as_view()),
    path("brand/<int:pk>", views.BrandDetail.as_view()),
    path("account/register/", views.CreateUserView.as_view()),
    path("account/<int:pk>", views.UserDetail.as_view()),

]