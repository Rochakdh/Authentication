from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomAuthToken

# Url Till This App : /user/

app_name = 'userauth'
router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
                  path('api-token-auth/', CustomAuthToken.as_view())
              ] + router.urls
