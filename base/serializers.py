from rest_framework import viewsets, serializers
from .models import Appointment, Billing,Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'



class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['appointment','amount_paid','due_balance','payable_amount','discount','total']

