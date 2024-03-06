from django.shortcuts import render

from rest_framework import generics

from .serializer import ProfileSerializer
from .models import Profile
# Create your views here.


class ProfileListView(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer