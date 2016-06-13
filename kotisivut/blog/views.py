from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from blog.models import Post

# Create your views here.
def posts_list(request):
	all_posts = Post.objects.all().order_by('-created_at')
	t=loader.get_template('blog/posts.html')
	c = Context({'all_posts': all_posts, })
	return HttpResponse(t.render(c))
