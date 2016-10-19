from django.test import TestCase, RequestFactory, Client
from main.models import viewCounter
from django.core.urlresolvers import resolve
from main.views import index, cv, projects
from django.shortcuts import render_to_response



# Create your tests here.
class indexTests(TestCase):

	def test_root_resolves_to_index_view(self):
		landing_page=resolve('/')
		self.assertEquals(landing_page.func, index)

	def test_returns_correct_value_for_views(self):

		#Luodaan viewCounter ilmentyma index-sivulle
		counter=viewCounter(counterName='index')
		counter.save()

		katselukerrat_aluksi=viewCounter.objects.get(counterName='index').views
		index=self.client.get('/')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='index').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)


	def test_uses_right_template(self):

		self.client = Client()

		counter=viewCounter(counterName='index')
		counter.save()

		index = self.client.get('/')

		self.assertTemplateUsed(
		index, 'main/index.html')

class cvTests(TestCase):

	def test_cv_resolves_to_cv_view(self):
		
		cv_page=resolve('/cv')
		self.assertEquals(cv_page.func, cv)

	def test_cv_returns_correct_views_value(self):

		counter=viewCounter(counterName='cv')
		counter.save()

		katselukerrat_aluksi=viewCounter.objects.get(counterName='cv').views
		index=self.client.get('/cv')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='cv').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)

	def test_uses_right_template(self):

		self.client = Client()

		counter=viewCounter(counterName='cv')
		counter.save()

		cv = self.client.get('/cv')
		#katselukerrat=viewCounter.objects.get(counterName='cv').views

		self.assertTemplateUsed(
		cv, 'main/cv.html')

class projectsTests(TestCase):

	def test_projects_resolves_to_projects_view(self):

		projects_page = resolve('/projects')
		self.assertEquals(projects_page.func, projects)

	def test_uses_correct_template(self):

		self.client = Client()
		
		counter=viewCounter(counterName='projects')
		counter.save()

		projects = self.client.get('/projects')

		self.assertTemplateUsed(
			projects, 'main/projects.html')


	def test_viewCounter_works(self):

		counter=viewCounter(counterName='projects')
		counter.save()

		katselukerrat_aluksi=viewCounter.objects.get(counterName='projects').views
		index=self.client.get('/projects')
		katselukerrat_lopuksi=viewCounter.objects.get(counterName='projects').views
		self.assertEquals(katselukerrat_aluksi+1, katselukerrat_lopuksi)

