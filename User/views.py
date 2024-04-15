from rest_framework.response import Response

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import ProfileSerializer, PaymentSerializer, UserTokenObtainSerializer, MessageSerializer
from .models import Profile, Payment, Messages
from .utils import SendMail
from rest_framework.pagination import PageNumberPagination


class LoginView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer

class ProfileListView(generics.ListCreateAPIView):
    
    search_fields = ['first_name', 'last_name',]
    filter_backends = (filters.SearchFilter,)
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    queryset = Profile.objects.all().order_by('created_date')
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    lookup_field = 'id'
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]



class PaymentListView(generics.ListCreateAPIView):
    
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        
        user = Profile.objects.get(id = request.user.id)
        
        if user.role == 2 :
            queryset = queryset.filter(payment_profile_id=request.user.id)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset= Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class MessageListView(generics.ListCreateAPIView):

    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    
    def patch(self, request, *args, **kwargs):
        print(request.data, 'dasdas')
        instance = Messages.objects.get(id=request.data['id'])
        instance.replied = True
        instance.save()
        data = request.data
        data['mail'] = instance.user.email
        SendMail(data)
        
        return Response({'stats': 'message'})