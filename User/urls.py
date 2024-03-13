from django.urls import path

from rest_framework.authtoken import views

from .views import ProfileListView, ProfileDetailView, PaymentListView, PaymentDetailView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='Profile-list'),
    path('profile/<id>', ProfileDetailView.as_view(), name='Profile-detail'),
    path('login/', views.obtain_auth_token, name='obtain-token'),
    path('payment/', PaymentListView.as_view(), name='payment-list'),
    path('payment/<id>', PaymentDetailView.as_view(), name='payment-detail')
]
