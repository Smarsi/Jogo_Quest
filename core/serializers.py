from django.contrib.auth.models import User, Group
from rest_framework import serializers

#import dos models
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PerguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perguntas
        fields = ["pergunta", "alternativa1", "alternativa2", "alternativa3", "alternativa4", "alternativa5", "resposta", "tema_pergunta"]

