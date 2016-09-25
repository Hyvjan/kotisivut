from __future__ import unicode_literals

from django.db import models

# Create your models here.
class viewCounter(models.Model):
	index='index'
	blog='blog'
	page_list=(
		(index, 'index'),
		(blog, 'blog'),
		)
	counterName=models.CharField(
		max_length=20,
		choices=page_list,
		)
	views=models.IntegerField(default=0)


	def __unicode__(self): 
		return self.views


