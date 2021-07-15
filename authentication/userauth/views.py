from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import customUsersDetailSearializers
from .permissions import CustomIsAuthenticated

# Create your views here.
USER = get_user_model()


class UserViewSet(ModelViewSet):
    """
    ViewSet for CRUD of USER object
    """
    http_method_names = ['get', 'put', 'patch', 'delete', 'post']
    serializer_class = customUsersDetailSearializers
    queryset = USER.objects.all()
    # authentication_classes = [TokenAuthentication]
    permission_classes = [CustomIsAuthenticated]
    lookup_field = 'username'
    lookup_url_kwarg = 'id'

    # def get_queryset(self):
    #     """
    #     :return: filtered queryset of the user itself only
    #     """
    #     super(UserViewSet, self).get_queryset()
    #     return self.queryset.filter(id=self.request.user.id)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': user.id,
        })
