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
	current_user = request.user
	my_tickets = Ticket.objects.filter(user=current_user)
	context = {'ticket_list': my_tickets}
	return render(request, 'myTickets.html', context)

@login_required(login_url='auth')
def planning(request):
	ticket_list = Ticket.objects.all().order_by('-clean_date')
	context = {'ticket_list': ticket_list}
	return render(request, 'planning.html', context)

@login_required(login_url='auth')
def profile(request):
	return render(request, 'profile.html', {})

@login_required(login_url='auth')
def buildings(request):
	return render(request, 'buildings.html', {})

@login_required(login_url='auth')
def submittedTickets(request):
	ticket_list = Ticket.objects.all()
	context = {'ticket_list': ticket_list}
	return render(request, 'submittedTickets.html', context)

@login_required(login_url='auth')
#Ticket detail, raises 404 error if the ticket is not found
def ticket(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	return render(request, 'ticket.html', {'ticket': ticket})

@login_required(login_url='auth')
def ticketForm(request):
	user = request.user
	client = Client.objects.filter(user=user)
	building_list = Building.objects.filter(owner=client[0])
	ticket_list = Ticket.objects.all()

	context = {'building_list': building_list, 'ticket_list': ticket_list}
	return render(request, 'ticketForm.html', context)
