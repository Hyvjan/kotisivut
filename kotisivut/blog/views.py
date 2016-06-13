from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def posts_list(request):
	t=loader.get_template('blog/posts.html')
	return HttpResponse(t.render())
	