from django.urls import path

from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='Profile'),
    path('profile/<id>', ProfileDetailView.as_view(), name='Profile'),
]
