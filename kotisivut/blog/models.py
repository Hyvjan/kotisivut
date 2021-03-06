from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __unicode__(self):
		return self.title