from rest_framework import generics
from rest_framework import permissions
from tasks.models import *
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.



class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Task.objects.filter()
    

class TaskREtiveDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'
