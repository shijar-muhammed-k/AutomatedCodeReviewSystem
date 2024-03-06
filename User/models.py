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
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self) :
        return self.first_name + " " + self.last_name