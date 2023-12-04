from django.shortcuts import render, redirect 
from library_app.views import *
from .forms import *


def home(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('book')
	else:
		form = StudentForm()


	return render(request, 'home.html', {'form': form})



def book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = BookForm()

	return render(request, 'book.html', {'form': form})