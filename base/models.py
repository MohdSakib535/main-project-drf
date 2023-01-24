from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=20)
    speacilist=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}-({self.speacilist})"

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    date=models.DateField()
    doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)


    def __str__(self):
        return f'Appointment with {self.doctor_name} '

class Billing(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount_paid=models.IntegerField()
    due_balance=models.IntegerField()
    payable_amount=models.IntegerField()
    discount = models.IntegerField()

    
    def __str__(self):
        return f'Billing for Appointment {self.appointment.id}'

    def total(self,*args,**kwargs):
        s1=self.amount_paid+self.due_balance-self.discount
        super(Billing,self).save(*args,**kwargs)
        return s1

