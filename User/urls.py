from django.urls import path

from rest_framework.authtoken import views

from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='Profile'),
    path('profile/<id>', ProfileDetailView.as_view(), name='Profile'),
    path('login/', views.obtain_auth_token, name='obtain-token')
]
