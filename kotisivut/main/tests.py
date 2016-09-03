from django.test import TestCase, RequestFactory
from main.models import viewCounter
from django.core.urlresolvers import resolve
from main.views import index



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
