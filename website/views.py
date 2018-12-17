from django.shortcuts import render

from .models import User, Building, Request

def home(request):
	return render(request, 'home.html', {})

def myTickets(request):
	return render(request, 'myTickets.html', {})

def planning(request):
	return render(request, 'planning.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def connect(request):
	return render(request, 'connect.html', {})

def submittedTickets(request):
	soonest_request_list = Request.objects.order_by('clean_date')[:5]
	context = {'soonest_request_list': soonest_request_list}
	return render(request, 'submittedTickets.html', context)

#Ticket detail, raises 404 error if the ticket is not found
def ticket(request, ticket_id):
	try:
		ticket = Request.objects.get(pk=ticket_id)
	except Request.DoesNotExist:
		raise Http404("Ticket does not exist")
	return render(request, 'ticket.html', {'ticket': ticket})

def ticketForm(request):
	return render(request, 'ticketForm.html', {})
