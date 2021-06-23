from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import customUsersDetailSearializers
from .models import customUseraDetails

# Create your views here.
USER = get_user_model()

class UserViewSet(ModelViewSet):
    """
    ViewSet for CRUD of USER object
    """
    http_method_names = ['get', 'put', 'patch', 'delete']
    serializer_class = customUsersDetailSearializers
    queryset = USER.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'