from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.http import HttpResponse, JsonResponse
from .models import Appointment, Billing,Doctor
from .serializers import AppointmentSerializer,DoctorSerializer,BillingSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models as django_models
from django_filters import  rest_framework as filter
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle



class Doctor_data(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class =DoctorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends=[filters.SearchFilter,]
    search_fields=['name','speacilist']


#     custom filter
class MyModelFilter(filter.FilterSet):
    date = filter.DateTimeFilter(field_name='date', lookup_expr='exact')
    class Meta:
        model =Appointment
        fields = ['date']


class AppointmentData(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends=[DjangoFilterBackend,]
    filter_class = MyModelFilter
    throttle_classes=[UserRateThrottle]
    


    # filter_backends=[filters.SearchFilter]
    # search_fields=['date']

 


class BillingData(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['due_balance']
    #     or
    # ordering_fields = '__all__'

  
