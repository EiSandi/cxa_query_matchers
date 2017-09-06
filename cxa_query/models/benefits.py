from django.db import models
from cxa_query.models import *

class Benefits (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=False)
	area_coverage = models.CharField(max_length=500, blank=False, null=True)
	basic_coverage = models.CharField(max_length=500, blank=False, null=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.name