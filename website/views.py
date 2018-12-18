from django.shortcuts import get_object_or_404, render, redirect
from .models import Client, Building, Ticket
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	print(username, password, user)
	if user is not None:
		login(request, user)
		return redirect('/home')
	else:
		return render(request, 'signIn.html', {})

def signUp(request):
	return render(request, 'signUp.html', {})

@login_required(login_url='auth')
def home(request):
	return render(request, 'home.html', {})

@login_required(login_url='auth')
def myTickets(request):
	return render(request, 'myTickets.html', {})

@login_required(login_url='auth')
def planning(request):
	return render(request, 'planning.html', {})

@login_required(login_url='auth')
def profile(request):
	return render(request, 'profile.html', {})

@login_required(login_url='auth')
def buildings(request):
	return render(request, 'buildings.html', {})

@login_required(login_url='auth')
def submittedTickets(request):
	soonest_ticket_list = Ticket.objects.order_by('clean_date')[:5]
	context = {'soonest_ticket_list': soonest_ticket_list}
	return render(request, 'submittedTickets.html', context)

@login_required(login_url='auth')
#Ticket detail, raises 404 error if the ticket is not found
def ticket(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	return render(request, 'ticket.html', {'ticket': ticket})

@login_required(login_url='auth')
def ticketForm(request):
	return render(request, 'ticketForm.html', {})
