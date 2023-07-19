from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer



# Create your views here.

def index(request):
    #return HttpResponse(".: Esta es la vista del modulo cliente :.")
    client = Cliente.objects.all()
    return render(request, 'cliente/index.html', {
        'client':client,
    })

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer