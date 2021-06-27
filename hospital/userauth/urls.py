from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Url Till This App : /user/

app_name = 'userauth'
router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [] + router.urls
