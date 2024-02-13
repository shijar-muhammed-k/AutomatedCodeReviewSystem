from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .analysis_code import analyze_code

from .models import tempFile

# Create your views here.
class test(ListCreateAPIView):
    
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        return JsonResponse({'success': True})
    
    def post(self, request, *args, **kwargs):
        db = tempFile()
        data = request.data
        db.name = data['file'].name
        db.file = data['file']
        db.upload_at = data['upload_at']
        db.save()
        report = analyze_code(str(db.file))
        return Response({'success': True, 'report': report})