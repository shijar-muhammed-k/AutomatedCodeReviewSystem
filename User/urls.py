from django.urls import path

from .views import ProfileListView, ProfileDetailView, PaymentListView, PaymentDetailView, LoginView, MessageListView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='Profile-list'),
    path('profile/<id>', ProfileDetailView.as_view(), name='Profile-detail'),
    path('login/', LoginView.as_view(), name='obtain-token'),
    path('payment/', PaymentListView.as_view(), name='payment-list'),
    path('payment/<id>', PaymentDetailView.as_view(), name='payment-detail'),
    path('messages/', MessageListView.as_view(), name='messages'),
]
