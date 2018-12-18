from django.contrib import admin

from .models import Client, Building, Ticket

admin.site.register(Client)
admin.site.register(Building)
admin.site.register(Ticket)
