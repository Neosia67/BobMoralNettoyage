from django.contrib import admin

from .models import User, Building, Ticket

admin.site.register(User)
admin.site.register(Building)
admin.site.register(Ticket)
