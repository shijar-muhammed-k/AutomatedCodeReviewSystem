from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializer import ProfileSerializer, PaymentSerializer
from .models import Profile, Payment
# Create your views here.


class ProfileListView(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]



class PaymentListView(generics.ListCreateAPIView):
    
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset= Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
