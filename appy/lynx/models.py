from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    # upload_to='images/' tells Django to upload all the images to the images folder on the server or S3 AWS
    profile_pic = models.ImageField(
        default='Default.png', null=True, blank=True, upload_to='images/')
    # FK for User. If the user is deleted, the profile is deleted as well
    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True)
