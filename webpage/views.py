from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def home(request):
	if request.method=="GET":
		return HttpResponse('YoYoYo')