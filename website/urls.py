from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auth$', views.auth, name='auth'),
    path('', views.auth, name='auth'),
    path('home/', views.home, name='home'),
    path('myTickets/', views.myTickets, name='myTickets'),
    path('planning/', views.planning, name='planning'),
    path('profile/', views.profile, name='profile'),
    path('submittedTickets/', views.submittedTickets, name='submittedTickets'),
    path('ticket/<int:ticket_id>/', views.ticket, name='ticket'),
    path('ticketForm/', views.ticketForm, name='ticketForm'),
]
