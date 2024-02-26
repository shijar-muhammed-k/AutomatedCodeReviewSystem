from django.shortcuts import render

from rest_framework import generics

from .serializer import ProfileSerializer
from .models import Profile
# Create your views here.


class ProfileListView(generics.ListCreateApiView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyApiView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer