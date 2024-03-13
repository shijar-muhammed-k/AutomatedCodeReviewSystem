from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(User):
    MALE = 1
    FEMALE = 2
    OTHERS = 3 
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (OTHERS, 'others'),
    )

    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    profession = models.CharField(max_length=25, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    credit_points = models.PositiveIntegerField(default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.first_name + " " + self.last_name


class Payment(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, name="payment_profile")
    amount = models.PositiveIntegerField()
    transcation_id = models.CharField(max_length=52, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)