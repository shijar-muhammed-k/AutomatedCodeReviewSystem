from django.db import models
from User.models import Profile

# Create your models here.
class Code(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    code_to_review = models.FileField(upload_to='code_to_review/', null=True)
    restructured_code = models.BooleanField(default=False)
    code_report = models.TextField()
    name = models.CharField(max_length=100)
    upload_at = models.DateTimeField(auto_now_add=True)


class tempFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='temp_files/', null=True)
    upload_at = models.DateField(null=True)
    

class AdminCredits(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    transaction = models.CharField(max_length=15, blank=True)
    date = models.DateField(null=True, auto_now_add=True, blank=True)