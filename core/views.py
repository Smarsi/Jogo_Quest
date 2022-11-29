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
    
    def post(self, request, format=None):
        response = []
        info = request.data
        for i in info:
            if(i[2] == "a"):
                resposta = 1
            if(i[2] == "b"):
                resposta = 2
            if(i[2] == "c"):
                resposta = 3
            if(i[2] == "d"):
                resposta = 4
            if(i[2] == "e"):
                resposta = 5

            data = {
                'pergunta': i[0], 
                'alternativa1': i[1][0], 
                'alternativa2': i[1][1], 
                'alternativa3': i[1][2], 
                'alternativa4': i[1][3], 
                'alternativa5': i[1][4], 
                'resposta': resposta,
                'tema_pergunta': 1
            }

            serializer = PerguntasSerializer(data=data)
            if serializer.is_valid():
                serializer.save()


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
