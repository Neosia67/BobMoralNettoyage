import os
from django.conf import settings
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(models.Model):
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    mail_addr = models.EmailField(primary_key=True, max_length=254, default="")
    phone_number = models.CharField(max_length=20, default="") # Peut-être 12 : +336XXXXXXXX
    address = models.CharField(max_length=120, default="")  # Pourquoi une addresse ?

    @property
    def get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def get_mail_addr(self):
        "Returns the person's full name."
        return '%s' % (self.mail_addr)
  

class Building(models.Model):
    address = models.CharField(primary_key=True, max_length=254, default="")


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    #FIXED Image Field
    img = models.ImageField(upload_to=settings.MEDIA_ROOT)
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
