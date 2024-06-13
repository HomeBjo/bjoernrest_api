from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import TodoSerializer
from .models import Todo


from telnetlib import STATUS
from django.http import HttpResponse
from django.core import serializers



class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at') 
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated auch später mit dem user
    
    def create(self, request):
        todo = Todo.objects.create(title= request.POST.get('title', ''), 
                                  description= request.POST.get('description', ''),
                                  user= request.user,
                                )
        serialized_obj = serializers.serialize('json', [todo, ]) 
        return HttpResponse(serialized_obj, content_type='application/json')