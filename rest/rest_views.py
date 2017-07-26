from rest_framework import viewsets
from django.contrib.auth.models import User
from rest.rest_serializers import *
from rest import models

'''
UserViewSet: 相当于django的视图
users: localhost:8080/api/users
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Userprofile.objects.all()
    #serializer_class :交给UserSerializer进行序列化
    serializer_class = UserprofileSerializer

class HostnameView(viewsets.ModelViewSet):

    queryset = models.Hostname.objects.all()

    serializer_class = HostSerializer

class SpeciesView(viewsets.ModelViewSet):

    queryset = models.Species.objects.all()

    serializer_class = SpeciesSerializer

class SaltrunView(viewsets.ModelViewSet):

    queryset = models.Saltrun.objects.all()

    serializer_class = SaltrunSerializer