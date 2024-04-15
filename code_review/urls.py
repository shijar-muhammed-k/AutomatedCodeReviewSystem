from django.urls import path
from .views import CheckCode, CodeFix, AdminBalanceListView

urlpatterns = [
    path('code/', CheckCode.as_view(), name='CodeReview'),
    path('fix/<id>', CodeFix.as_view(), name='code-fix'),
    path('balance', AdminBalanceListView.as_view(), name='balance'),
]
