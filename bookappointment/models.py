from django.db import models
import datetime


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class sub_category(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Client(models.Model):
    pass


class BookAppointment(models.Model):
    time = models.TimeField(blank=False, null=True)
    date = models.DateField(blank=False, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    appointment_with = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.date


class Questions(models.Model):
    question = models.TextField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answers(models.Model):
    answer = models.TextField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class FeedbackRating(models.Model):
    given_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    given_to = models.ForeignKey(Client, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return self.feedback
