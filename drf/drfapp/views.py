from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Optional for authentication

from .models import *
from .serializers import *

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated]  # Uncomment for authentication

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'
