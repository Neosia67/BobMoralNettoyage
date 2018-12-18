from django.shortcuts import get_object_or_404, render, redirect
from .models import Client, Building, Ticket, User
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
	username = request.POST.get('username')
	password = request.POST.get('password')
	email = request.POST.get('email')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		#User already exists
		return render(request, 'signUp.html', {})
	else:
		#User does not exists
		try:
			match = User.objects.get(email=email)
			return render(request, 'signUp.html', {})
		except User.DoesNotExist:
			User.objects.create_user(username, email=email, password=password)
			return render(request, 'signIn.html', {})


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
	soonest_ticket_list = Ticket.objects.all()
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
