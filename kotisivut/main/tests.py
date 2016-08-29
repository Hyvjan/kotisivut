
from django.test import TestCase, RequestFactory
from main.models import viewCounter
from django.core.urlresolvers import resolve
from .views import index



# Create your tests here.
class indexTests(TestCase):

	@classmethod
	def setUpClass(cls):
		request_factory = RequestFactory()
		cls.request = request_factory.get('/')
		cls.request.session = {}

	def test_viewCounter_index_works(self):
		origin_value = viewCounter.objects.get(counterName='index')
		index = resolve('/')
		new_value = viewCounter.objects.get(counterName='index')
		self.assertEquals(origin_value+1, new_value)

			
	@classmethod
	def tearDownClass(cls):
		pass