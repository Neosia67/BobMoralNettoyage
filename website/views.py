from django.shortcuts import render

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
	return render(request, 'submittedTickets.html', {})

def ticket(request):
	return render(request, 'ticket.html', {})

def ticketForm(request):
	return render(request, 'ticketForm.html', {})