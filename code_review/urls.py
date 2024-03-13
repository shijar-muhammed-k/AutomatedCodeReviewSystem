from django.urls import path
from .views import test, CodeFix

urlpatterns = [
    path('code/', test.as_view(), name='CodeReview'),
    path('fix/<id>', CodeFix.as_view(), name='code-fix'),
]
