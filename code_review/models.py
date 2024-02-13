from django.db import models
from User.models import Profile

# Create your models here.
class Code(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    code_to_review = models.FileField(upload_to='code_to_review/', null=True)
    restructured_code = models.FileField(upload_to='restructured_code/', null=True)
    code_report = models.TextField()


class tempFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='temp_files/', null=True)
    upload_at = models.DateField(null=True)