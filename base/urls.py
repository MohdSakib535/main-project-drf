from django.urls import path
from . import views

urlpatterns = [
    path('c/', views.create_appointment, name='create_appointment'),
    path('l/', views.list_appointments, name='list_appointments'),
    path('cb/<int:appointment_id>/', views.create_bill, name='create_bill'),
]