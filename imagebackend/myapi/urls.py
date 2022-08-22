from django.urls import path, include
from django.views.generic import base
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'image', views.Showdata, basename='image')
urlpatterns = [
    path('', include(router.urls)),
]
