from django.shortcuts import render
from rest_framework import viewsets
from escola.models import *
from escola.serializer import *

# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer