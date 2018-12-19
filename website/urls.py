from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auth$', views.auth, name='auth'),
    path('', views.auth, name='auth'),
    path('home/', views.home, name='home'),
    path('myTickets/', views.myTickets, name='myTickets'),
    path('planning/', views.planning, name='planning'),
    path('profile/', views.profile, name='profile'),
    path('signUp/', views.signUp, name="signUp"),
    path('submittedTickets/', views.submittedTickets, name='submittedTickets'),
    path('ticket/<int:ticket_id>/', views.ticket, name='ticket'),
    path('ticketForm/', views.ticketForm, name='ticketForm'),
    path('addUser/', views.addUser, name='addUser'),
    path('ticketFormPost/', views.ticketFormPost, name='ticketFormPost'),
]
