from django.shortcuts import render, redirect
from .models import BookAppointment, Category, sub_category, Customer,FeedbackRating
from .forms import AppointmentForm
import datetime
from django.http import HttpResponse
from django.contrib import messages
from .filters import SubcategoryForm,RatingFilterForm


# Create your views here.


def Appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'appointment booked successfully')

        return render(request, 'appointment_schedular.html')

    return render(request, 'appointment_schedular.html')


def SubcategoryFilter(request):
    category_list = sub_category.objects.all()
    category_filter = SubcategoryForm(request.GET, queryset=category_list)
    return render(request, 'category_list.html', {'filter': category_filter})


def RatingFilter(request):
    rating = FeedbackRating.objects.filter(rating__exact=request)
    rating_filter = RatingFilterForm(request.GET, queryset=rating)
    return render(request, '', {'filter':rating_filter})

