"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.urls import include, path
from . import views
from .views import create_pet, pet_detail, petImage, product_scan, product_name, product_frontPicture
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Account
    path("accounts/", include("django.contrib.auth.urls")),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    path('paw_auth/', include('paw_auth.urls')),

    #Pet
    path('create_pet/', create_pet.as_view()),
    path('pet_detail/<int:pk>/', pet_detail.as_view()),
    path('uploads/', petImage.as_view(),),

    #Scan
    path('product_scan/', product_scan, name='product_scan'),
    path('products/', product_name.as_view(), name='product_name'),


]