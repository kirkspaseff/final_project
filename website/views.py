from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("Welcome to the homepage")
# Create your views here.

