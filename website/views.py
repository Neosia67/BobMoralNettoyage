from django.shortcuts import get_object_or_404, render

from .models import User, Building, Ticket

def home(request):
	return render(request, 'home.html', {})

def myTickets(request):
	return render(request, 'myTickets.html', {})

def planning(request):
	return render(request, 'planning.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def buildings(request):
	return render(request, 'buildings.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def connect(request):
	return render(request, 'connect.html', {})

def submittedTickets(request):
	soonest_request_list = Request.objects.order_by('clean_date')[:5]
	context = {'soonest_ticket_list': soonest_ticket_list}
	return render(request, 'submittedTickets.html', context)

#Ticket detail, raises 404 error if the ticket is not found
def ticket(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)
	return render(request, 'ticket.html', {'ticket': ticket})

def ticketForm(request):	
	return render(request, 'ticketForm.html', {})
