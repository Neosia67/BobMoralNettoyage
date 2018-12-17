import os
from django.conf import settings
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    mail_addr = models.EmailField(primary_key=True, max_length=254, default="")
    phone_number = models.CharField(max_length=20, default="") # Peut-être 12 : +336XXXXXXXX
    address = models.CharField(max_length=120, default="")  # Pourquoi une addresse ?
    def __str__(self):
        return "%s" % (self.mail_addr)

class Building(models.Model):
    address = models.CharField(primary_key=True, max_length=254, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="None")
    def __str__(self):
        return "%s" % (self.address)

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    #FIXED Image Field
    img = models.ImageField(upload_to=settings.MEDIA_ROOT + '_' + str(user) + '_' + str(building), default="image/default.png")
    floor = models.PositiveIntegerField(default=0)
    ORIENT = (
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
    orientation = models.CharField(max_length=3, choices=ORIENT, default="N")
    clean_date = models.DateTimeField("cleaning date")

    def is_img_in_db(self):
        return self.img
