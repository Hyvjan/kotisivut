from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def posts_list(request):
	all_posts = Post.objects.all().order_by('-created_at')
	return render_to_response('blog/posts.html', {'all_posts': all_posts} , RequestContext(request) )

@login_required
def add_post(request):
	context=RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			messages.add_message(request, messages.INFO, "Postauksesi on lisatty.")
			return HttpResponseRedirect('/blog')
		else:
			print form.errors
	else:
		form=PostForm()
	return render_to_response('blog/add_post.html', {'form':form}, context)

@login_required
def delete_post(request, pk):
	post=get_object_or_404(Post, pk=pk)
	post.delete()
	messages.add_message(request, messages.INFO, "Postaus on poistettu onnistuneesti")
	return redirect('posts_list')

@login_required
def edit_post(request, pk):
	context=RequestContext(request)
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=True)
			return redirect('posts_list')
	else:
		form=PostForm(instance=post)
	return render_to_response('blog/add_post.html', {'form':form}, context)


