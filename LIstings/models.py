from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

client_type =(('Arch','Architects'),('IntDes','InteriorDesiginers'),('ArchInte','Architercts_InteriorDesigners'),('Contr','Contractors'))

class IungoUser(AbstractUser):
    ClientType = models.CharField(max_length=30, choices=client_type)
    ProfileImage = models.ImageField(upload_to='media/profile_images/')