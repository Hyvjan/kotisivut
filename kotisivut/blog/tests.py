from django.test import TestCase, RequestFactory, Client, modify_settings
from main.models import viewCounter
from blog.models import Post
from django.core.urlresolvers import resolve, reverse
from blog.views import posts_list, add_post, delete_post, edit_post
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render_to_response
from .forms import PostForm
from django.contrib import messages
import mock

# Create your tests here.
class indexTests(TestCase):

	def test_blog_resolves_to_posts_list_view(self):
		post_lists=resolve('/blog')
		self.assertEquals(post_lists.func, posts_list)

	def test_returns_correct_html(self):

		#Luodaan viewCounter ilmentyma index-sivulle
		counter=viewCounter(counterName='blog')
		counter.save()

		#Testataan, etta index-nakyman lataaminen kasvattaa laskuria yhdella
		katselukerrat_aluksi=viewCounter.objects.get(counterName='blog').views
		index=self.client.get('/blog')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='blog').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)


	def test_index_query_for_all_posts_works(self):

		post1=Post(title="post1", content="test posting 1")
		post1.save()

		post2=Post(title="post2", content="test posting 2")
		post2.save()

		all_posts = Post.objects.all().order_by('-created_at')

		self.assertEquals(len(all_posts), 2)
		self.assertEquals(all_posts[0].title, u'post2')
		self.assertEquals(all_posts[1].title, u'post1')


class add_postTests(TestCase):


	def test_unlogged_user_cannot_access_add_post_view(self):
		
		self.factory = RequestFactory()
		request = self.factory.get('/blog/add_post/')
		request.user = AnonymousUser()
		response = add_post(request)

		self.assertEqual(response.status_code, 302)


	def test_logged_in_user_can_access(self):

		
		self.factory = RequestFactory()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		
		request = self.factory.get('/blog/add_post/')
		request.user = self.user
		response = add_post(request)

		self.assertEqual(response.status_code, 200)


	def test_add_post_form_works_with_correct_data(self):

		from pprint import pformat

		data={'title':'test blogging', 'content': 'This is test blogging content' }
		form = PostForm(data=data)
		form.save(commit=True)

		all_posts = Post.objects.all().order_by('-created_at')
		self.assertEquals(len(all_posts), 1)
		self.assertEquals(all_posts[0].title, u'test blogging')
		self.assertEquals(all_posts[0].content, u'This is test blogging content')

	def test_add_post_form_gives_error_if_title_missing(self):

		from pprint import pformat

		data={'title':'', 'content': 'This is test blogging content' }
		form = PostForm(data=data)
		

		self.assertEquals(form.errors, {'title': [u'This field is required.']})

	def test_add_post_form_gives_error_if_content_missing(self):

		from pprint import pformat

		data={'title':'test blogging', 'content': '' }
		form = PostForm(data=data)
		

		self.assertEquals(form.errors, {'content': [u'This field is required.']})

		
class delete_postTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		post1 = Post(title="post1", content="test posting 1")
		post1.save()

		post2=Post(title="post2", content="test posting 2")
		post2.save()

	def test_unlogged_user_cannot_access_delete_post_view(self):
		
		self.factory = RequestFactory()
		request = self.factory.get('/blog/delete_post/1')
		request.user = AnonymousUser()
		response = delete_post(request)

		self.assertEqual(response.status_code, 302)
		all_posts = Post.objects.all().order_by('-created_at')
		self.assertEquals(len(all_posts), 2)

	
	def test_logged_in_user_can_access_delete_post(self):

		self.client= Client()
		self.user=User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		
		self.client.login(username='john', password='johnpassword')
		response=self.client.get('/blogdelete_post/2')

		self.assertEqual(response.status_code, 302)		
		all_posts = Post.objects.all().order_by('-created_at')
		self.assertEquals(len(all_posts), 1)

class edit_PostTest(TestCase):

	@classmethod 
	def setUpTestData(cls):
		post1 = Post(title="post1", content="test posting 1")
		post1.save()

		post2=Post(title="post2", content="test posting 2")
		post2.save()

	def test_unlogged_user_cannot_edit_post(self):

		self.factory = RequestFactory()
		request = self.factory.get('/blogedit_post/1')
		request.user = AnonymousUser()
		response = edit_post(request)

		self.assertEqual(response.status_code, 302)
		

	def test_logged_user_can_access_edit_post(self):

		self.client=Client()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		self.client.login(username='john', password='johnpassword')
		response = self.client.get('/blogedit_post/1')

		self.assertEqual(response.status_code, 200)