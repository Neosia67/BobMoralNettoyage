from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myTickets/', views.myTickets, name='my tickets'),
    path('planning/', views.planning, name='planning'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('connect/', views.connect, name='connect'),
    path('submittedTickets/', views.submittedTickets, name='submittedTickets'),
    path('ticket/', views.ticket, name='ticket'),
    path('ticketForm/', views.ticketForm, name='ticketForm'),
]
