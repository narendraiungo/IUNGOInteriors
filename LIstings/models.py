from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

client_type = (('Architects', 'Architects'), ('InteriorDesigners', 'InteriorDesigners'),
               ('Architects_interiordesigenrs', 'Architects_interiordesigenrs'),
               ('Contractors', 'Contractors'))


class IungoUser(AbstractUser):
    ClientType = models.CharField(max_length=30, choices=client_type)
    client_category = models.CharField(max_length=30)
    # ProfileImage = models.ImageField(upload_to='media/profile_images/')


class Architects(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Architects_interiordesigenrs(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class InteriorDesigners(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contractors(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
