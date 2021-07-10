import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError


class Doctor(models.Model):
    firstname = models.CharField('First Name', max_length=200)
    lastname = models.CharField('Last Name', max_length=200)
    admission_date = models.DateField('Admission Date')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Place(models.Model):
    name = models.CharField('Name', max_length=200)
    active = models.BooleanField( default=True)
    def __str__(self):
        return self.name

class Address(models.Model):
    country = models.CharField('Country', max_length=200)
    state = models.CharField('State', max_length=200)
    city = models.CharField('City', max_length=200)
    district = models.CharField('district', max_length=200)
    street = models.CharField('Street', max_length=200)
    number = models.IntegerField('Number')
    place = models.OneToOneField(Place, on_delete=models.CASCADE)


class Day_Of(models.Model):
    class Meta:
        verbose_name = ("Day Of")
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
    

    WEEKDAYS = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    day_of = models.IntegerField("Day Of",choices=WEEKDAYS)
    doctor = models.ForeignKey(Doctor, on_delete=CASCADE)

    class Meta:
        unique_together = ['day_of', 'doctor']
    def __str__(self):
        return f"{self.day_of}"

    def clean(self):
        if Schedule.objects.filter(doctor=self.doctor, date__week_day=self.day_of):
            raise ValidationError('This date has an schedule')
        return super().clean()

class Schedule(models.Model):
    date = models.DateField('Date')
    place = models.ForeignKey(Place, on_delete=CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=CASCADE)
    
    class Meta:
        unique_together = ('date', 'doctor')

    def __str__(self):
        return f"{self.doctor} {self.place} {self.date}"

    def convert_weekday(self):
        if self.date.weekday() == 0: return 2
        if self.date.weekday() == 1: return 3
        if self.date.weekday() == 2: return 4
        if self.date.weekday() == 3: return 5
        if self.date.weekday() == 4: return 6
        if self.date.weekday() == 5: return 7
        if self.date.weekday() == 6: return 1
    
    def clean(self):

        if Day_Of.objects.filter(doctor=self.doctor, day_of = self.convert_weekday()).exists():
            print(self.date.weekday())
            raise ValidationError("This is a day of")
        return super().clean()

    def save(self):
        print(self.date.weekday())
        
        return super().save()
        
        