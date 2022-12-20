from django.shortcuts import render
from rest_framework import generics
from .models import book
from .serializers import bookSerializer

# Create your views here.
class bookList(generics.ListCreateAPIView):
    queryset=book.objects.all()
    serializer_class=bookSerializer

class bookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=book
    serializer_class=bookSerializer