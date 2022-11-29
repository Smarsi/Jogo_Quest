from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#import dos serializers
from .serializers import PerguntasSerializer

#import de informacoes
from .models import *

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = "Olá mundo"
        return Response(content)


class GetPerguntas(APIView):
    def get(self, request, format=None):
        perguntas = Perguntas.objects.all()
        serializer = PerguntasSerializer(perguntas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CadPerguntas(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        info = request.data


        
        print(request.data)

        content = "Olá mundo"
        return Response(content)
