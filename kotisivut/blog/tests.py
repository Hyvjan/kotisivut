from django.test import TestCase, RequestFactory
from main.models import viewCounter
from blog.models import Post
from django.core.urlresolvers import resolve, reverse
from blog.views import posts_list, add_post
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render_to_response

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


	"""	
class delete_postTests(TestCase):

	def test_unlogged_user_cannot_access_delete_post_view(self):
		
		self.factory = RequestFactory()
		request = self.factory.get('/blog/delete_post/')
		request.user = AnonymousUser()
		response = add_post(request)

		self.assertEqual(response.status_code, 302)

	def test_logged_in_user_can_access_delete_post(self):

		
		self.factory = RequestFactory()
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		
		request = self.factory.get('/blog/add_post/')
		request.user = self.user
		response = add_post(request)

		self.assertEqual(response.status_code, 200)		

"""