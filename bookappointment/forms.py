from django import forms
from .models import BookAppointment


class AppointmentForm(forms.Form):

    class Meta:
        model = BookAppointment
        fields=['date','time','appointment_with']