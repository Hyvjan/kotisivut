from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
	all_posts = Post.objects.all().order_by('-created_at')
	return render_to_response('blog/posts.html', {'all_posts': all_posts, })

@login_required
def add_post(request):
	context=RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect('posts_list')
		else:
			print form.errors
	else:
		form=PostForm()
	return render_to_response('blog/add_post.html', {'form':form}, context)

@login_required
def delete_post(request, pk):
	post=get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('posts_list')