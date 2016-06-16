from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
def posts_list(request):
	all_posts = Post.objects.all().order_by('-created_at')
	t=loader.get_template('blog/posts.html')
	c = Context({'all_posts': all_posts, })
	return HttpResponse(t.render(c))


def add_post(request):
	context=RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect(index)
		else:
			print form.errors
	else:
		form=PostForm()
	return render_to_response('blog/add_post.html', {'form':form},context)