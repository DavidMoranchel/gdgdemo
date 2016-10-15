from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Info(models.Model):
	title = models.CharField(max_length=55,blank=False)
	description = models.CharField(max_length=255,blank=False)

	def __str__(self):
		return self.title