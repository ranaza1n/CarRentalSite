from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=22)
    phone = models.CharField(max_length=12)
    msg = models.TextField()
    date = models.DateField()

class Car_Selection(models.Model):
    model = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    vehicle_id = models.CharField(max_length=15)
    seating_capacity = models.CharField(max_length=15)
    rental_rate = models.CharField(max_length=15)
    Location = models.CharField(max_length=35)

class Rental_History(models.Model):
    model = models.CharField(max_length=35)
    memberID= models.CharField(max_length=35)
    vehicle_id = models.CharField(max_length=35)
    pickup = models.CharField(max_length=35)
    returntime = models.CharField(max_length=35)

class Revenue_Report(models.Model):
    model = models.CharField(max_length=35)
    lateFeeRevenue = models.CharField(max_length=35)
    vehicle_id = models.CharField(max_length=35)
    ReservationRevenue = models.CharField(max_length=35)
class Location_Pref_Report(models.Model):
    NofReservations = models.CharField(max_length=35)
    TotalHours= models.CharField(max_length=35)
    Location = models.CharField(max_length=55)
    Month = models.CharField(max_length=35)
class Frequent_User_Report(models.Model):
    MemberID = models.CharField(max_length=35)
    DrivingPlan= models.CharField(max_length=35)
    NofReservations = models.CharField(max_length=35)
