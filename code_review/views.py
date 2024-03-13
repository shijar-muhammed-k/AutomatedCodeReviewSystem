from rest_framework.generics import (GenericAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from .analysis_code import analyze_code, fix_code

from .models import tempFile

# Create your views here.
class test(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    
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
    

class CodeFix(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def deduct_amount(self):
        profile = self.request.user.profile
        profile.credit_points -= 10
        profile.save()

    def get_object(self):
        return tempFile.objects.get(id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = str(instance.file)
        return Response(file_path)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        # report = fix_code(file)
        reports = fix_code(str(instance.file))
        print(reports)
        self.deduct_amount()
        file_path = 'media/' + str(instance.file)
        FilePointer = open(file_path, 'r')
        response = HttpResponse(FilePointer,content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename=NameOfFile'
        return response
    
    """
    front-end code for this to work (in react)
handleDownload(id, filename) {
fetch(`http://127.0.0.1:8000/example/download/${id}/`).then(
    response => {
    response.blob().then(blob => {
    let url = window.URL.createObjectURL(blob);
    let a = document.createElement("a");
    console.log(url);
    a.href = url;
    a.download = filename;
    a.click();
    });
});
}
"""