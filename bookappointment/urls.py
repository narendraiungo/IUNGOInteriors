from django.urls import path
from bookappointment import views


urlpatterns=[
    path('bookappointment/',views.Appointment,name='bookappointment'),
    path('scsearch/',views.SubcategoryFilter,name='subcategory'),
    path('ratesearch/',views.RatingFilter,name='ratesearch'),
]