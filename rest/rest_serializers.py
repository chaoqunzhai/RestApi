from rest_framework import  serializers
from django.contrib.auth.models import User
from rest import models

'''
REST 序列化
#定义显示表里的哪个字段
'''



class UserprofileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Userprofile
        fields = ('name', 'email','status_type')

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hostname
        depth = 2
        fields = ('ip','disk','cpu','kernel','species_type','role_type','source')


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Species
        fields = ('species_name','date','phone')

class SaltrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saltrun
        fields = ('ip','fun','fun_args','salt_callable','job','date','statues','histroy')