from django.test import TestCase, RequestFactory
from main.models import viewCounter
from django.core.urlresolvers import resolve
from main.views import index



# Create your tests here.
class indexTests(TestCase):
	def test_root_resolves_to_main_view(self):
		landing_page=resolve('/')
		self.assertEquals(landing_page.func, index)