from django.test import TestCase, RequestFactory, Client
from main.models import viewCounter
from django.core.urlresolvers import resolve
from main.views import index, cv
from django.shortcuts import render_to_response



# Create your tests here.
class indexTests(TestCase):

	def test_root_resolves_to_index_view(self):
		landing_page=resolve('/')
		self.assertEquals(landing_page.func, index)

	def test_returns_correct_html(self):

		#Luodaan viewCounter ilmentyma index-sivulle
		counter=viewCounter(counterName='index')
		counter.save()

		katselukerrat_aluksi=viewCounter.objects.get(counterName='index').views
		index=self.client.get('/')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='index').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)

class cvTests(TestCase):

	def test_cv_resolves_to_cv_view(self):
		
		cv_page=resolve('/cv')
		self.assertEquals(cv_page.func, cv)

	def test_cv_returns_correct_html(self):
		
		self.factory = RequestFactory()
		request = self.factory.get('/cv')

		response = cv(request)

		self.assertEqual(response.status_code, 200)

	def test_uses_right_template(self):

		self.client = Client()
		cv = self.client.get('/cv')

		self.assertEquals(
		cv.content,
		render_to_response("main/cv.html").content
		)
