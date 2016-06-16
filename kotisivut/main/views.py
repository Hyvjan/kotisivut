from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
	t=loader.get_template('main/index.html')
	return HttpResponse(t.render())

