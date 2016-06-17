from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
	return render_to_response('main/index.html')

