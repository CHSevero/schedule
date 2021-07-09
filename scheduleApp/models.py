from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Doctor(models.Model):
    firstname = models.CharField('Nome', max_length=200)
    lastname = models.CharField('Sobrenome', max_length=200)
    admisson_date = models.DateField('Data de Admissão')
    active = models.BooleanField(default=True)

class Place(models.Model):
    name = models.CharField('Nome', max_length=200)
    active = models.BooleanField('Ativo', default=True)

class Address(models.Model):
    country = models.CharField('País', max_length=200)
    state = models.CharField('Estado', max_length=200)
    city = models.CharField('Cidade', max_length=200)
    district = models.CharField('Bairro', max_length=200)
    street = models.CharField('Rua', max_length=200)
    number = models.IntegerField('Numero')
    place = models.OneToOneField(Place, on_delete=models.CASCADE)


class Day_Of(models.Model):
    MONDAY = "seg"
    TUESDAY = "ter"
    WEDNESDAY = "qua"
    THURSDAY = "qui"
    FRIDAY = "sex"
    SATURDAY = "sab"
    SUNDAY = "dom"

    WEEKDAYS = [
        (MONDAY, 'Segunda'),
        (TUESDAY, 'Terça'),
        (WEDNESDAY, 'Quarta'),
        (THURSDAY, 'Quinta'),
        (FRIDAY, 'Sexta'),
        (SATURDAY, 'Sabado'),
        (SUNDAY, 'Domingo'),
    ]

    day_of = models.CharField("Dia de folga", max_length=15, choices=WEEKDAYS)
    doctor = models.OneToOneField(Doctor, on_delete=CASCADE)

class Schedule(models.Model):
    date = models.DateField('Date')
    place = models.OneToOneField(Place, on_delete=CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=CASCADE)

    