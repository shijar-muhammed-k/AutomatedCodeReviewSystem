from rest_framework.generics import (GenericAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .analysis_code import analyze_code, fix_code

from .models import tempFile, Code
from User.models import Profile
from .serializer import CodeSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CheckCode(GenericAPIView):
    
    def get_queryset(self):
        user = Profile.objects.get(id=self.request.user.id)
        queryset = Code.objects.all()
        
        if user.role == 2:
            return queryset.filter(user=user.id).order_by('upload_at')

        search_param = self.request.GET.get('search')
        if search_param:
            queryset = queryset.filter(user__first_name__contains=search_param)

        return queryset.order_by('upload_at')
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        serializer = CodeSerializer(page, many=True)
        return paginator.get_paginated_response({
            'success': True,
            'data': serializer.data,
        })
    
    def post(self, request, *args, **kwargs):
        
        if (request.user.is_authenticated):
            db = Code()
            data = request.data
            db.name = data['file'].name
            db.code_to_review = data['file']
            db.upload_at = data['upload_at']
            db.user = Profile.objects.get(id = request.user.id)
            db.save()
            report = analyze_code(str(db.code_to_review))
            db.code_report = report
            db.save()
            return Response({'success': True, 'report': report, 'id': db.id})
            

        else :
            db = tempFile()
            data = request.data
            db.name = data['file'].name
            db.file = data['file']
            print(data['file'].size)
            db.upload_at = data['upload_at']
            db.save()
            print(f'media/{str(db.file)}')
            report = analyze_code(str(db.file))

            return Response({'success': True, 'report': report})
    

class CodeFix(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def deduct_amount(self):
        profile = self.request.user.profile
        profile.credit_points -= 10
        profile.save()

    def get_object(self):
        return Code.objects.get(id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = str(instance.code_to_review)
        return Response(file_path)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        # report = fix_code(file)
        reports = fix_code(str(instance.code_to_review))
        print(reports)
        if(instance.restructured_code == False):
            self.deduct_amount()
            instance.restructured_code = True
            instance.save()
        file_path = 'media/' + str(instance.code_to_review)
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