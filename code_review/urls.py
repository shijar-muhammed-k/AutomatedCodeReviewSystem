from django.urls import path
from .views import test

urlpatterns = [
    path('code/', test.as_view(), name='CodeReview'),
]
