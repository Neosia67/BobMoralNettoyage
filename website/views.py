from django.shortcuts import get_object_or_404, render, redirect
from .models import Client, Building, Ticket, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	print(username, password, user)
	if user is not None:
		login(request, user)
		client = Client.objects.get(user=user)
		if client.role == "client":
			is_a_client = True
		else:
			is_a_client = False
		print(client.role, is_a_client)
		return render(request, 'home.html', {'is_a_client': is_a_client})
	else:
		return render(request, 'signIn.html', {})

def signUp(request):
	return render(request, 'signup.html')

def addUser(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	fn = request.POST.get('firstname')
	ln = request.POST.get('lastname')
	email = request.POST.get('email')
	telephone = request.POST.get('telephone')
	print(username, password, email)
	user = authenticate(request, username=username, password=password)
	if user is None:
		new_user = User.objects.create_user(username, email, password)
		new_user.is_active = True
		new_user.save()
		client = Client(user=new_user, first_name=fn, last_name=ln, phone_number=telephone)
		client.save()
		return redirect('/')
	redirect('addUser')

@login_required(login_url='auth')
def home(request, new_context={}):
	return render(request, 'home.html', new_context)

@login_required(login_url='auth')
def myTickets(request):
	user = request.user
	client = Client.objects.filter(user=user)
	my_tickets = Ticket.objects.filter(user=client[0])
	context = {'ticket_list': my_tickets}
	return render(request, 'myTickets.html', context)

@login_required(login_url='auth')
def planning(request):
	ticket_list = Ticket.objects.filter(status='AC').order_by('-clean_date')
	context = {'ticket_list': ticket_list}
	return render(request, 'planning.html', context)

@login_required(login_url='auth')
def profile(request):
	user = request.user
	client = Client.objects.filter(user=user)
	context = {'current_user': client[0], 'email': user.email}
	return render(request, 'profile.html', context)

@login_required(login_url='auth')
def buildings(request):
	user = request.user
	client = Client.objects.filter(user=user)
	building_list = Building.objects.filter(owner=client[0])
	context = {'building_list': building_list}
	return render(request, 'buildings.html', context)

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

def ticketFormPost(request):
	user = request.user
	client = Client.objects.filter(user=user)
	buildingAddress = request.POST.get('building')
	building = Building.objects.filter(address=buildingAddress)
	floor = request.POST.get('floor')
	orientation = request.POST.get('orientation')
	photo = 'client_{0}/{1}'.format(client[0].phone_number, request.POST.get('inputFile'))
	date = request.POST.get('date')
	hour = request.POST.get('hour')
	cleanDate = date + ' ' + hour
	print(building, floor, orientation, date, hour)
	ticket = Ticket(user=client[0], building=building[0], floor=floor, img=photo, status="EC", orientation=orientation, clean_date=cleanDate)
	ticket.save()
	context = {
		'is_a_client': True
	}
	response = home(request, context)
	return response

def buildingPost(request):
	user = request.user
	client = Client.objects.filter(user=user)
	address = request.POST.get('address')
	complement = request.POST.get('complement')
	floor_nb = request.POST.get('floors')
	building = Building(address=address, complement=complement, floor_nb=floor_nb, owner=client[0])
	building.save()
	return redirect('buildings')


def acceptTicket(request):
	ticket_id = request.POST.get('id')
	ticket = Ticket.objects.get(id=ticket_id)
	ticket.status = 'AC'
	ticket.save()
	return redirect('submittedTickets')

def refuseTicket(request):
	ticket_id = request.POST.get('id')
	ticket = Ticket.objects.get(id=ticket_id)
	ticket.status = 'RE'
	ticket.save()
	return redirect('submittedTickets')
