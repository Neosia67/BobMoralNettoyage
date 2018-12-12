from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    mail_addr = models.CharField(max_length=60, default="")
    phone_number = models.CharField(max_length=20, default="") # Peut-être 12 : +336XXXXXXXX
    address = models.CharField(max_length=120, default="") 

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #TODO Image Field
    floor = models.PositiveSmallIntegerField(default=0)
    orientation = (
    ("N", "Nord"),
    ("NNE", "Nord-Nord-Est"),
    ("NE", "Nord-Est"),
    ("ENE", "Est-Nord-Est"),
    ("E", "Est"),
    ("SE", "Est-Sud-Est"),
    ("SE", "Sud-Est"),
    ("SSE", "Sud-Sud-Est"),
    ("S", "Sud"),
    ("SSO", "Sud-Sud-Ouest"),
    ("SO", "Sud-Ouest"),
    ("OSO", "Ouest-Sud-Ouest"),
    ("O", "Ouest"),
    ("ONO", "Ouest-Nord-Ouest"),
    ("NO", "Nord-Ouest"),
    ("NNO", "Nord-Nord-Ouest")
    )
    clean_date = models.DateTimeField("cleaning date")
