from django.urls import path
from .views import CheckCode, CodeFix

urlpatterns = [
    path('code/', CheckCode.as_view(), name='CodeReview'),
    path('fix/<id>', CodeFix.as_view(), name='code-fix'),
]
