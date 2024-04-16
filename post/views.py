from django.shortcuts import render
from django.http import HttpResponse

# create a function
def home(request):
	
	return HttpResponse("<h1>Welcome to GeeksforGeeks</h1>")
