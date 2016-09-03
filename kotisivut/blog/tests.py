from django.test import TestCase, RequestFactory
from main.models import viewCounter
from django.core.urlresolvers import resolve
from blog.views import posts_list

# Create your tests here.
class indexTests(TestCase):

	def test_blog_resolves_to_posts_list_view(self):
		post_lists=resolve('/blog')
		self.assertEquals(post_lists.func, posts_list)

	def test_returns_correct_html(self):

		#Luodaan viewCounter ilmentyma index-sivulle
		counter=viewCounter(counterName='blog')
		counter.save()

		katselukerrat_aluksi=viewCounter.objects.get(counterName='blog').views
		index=self.client.get('/blog')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='blog').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)