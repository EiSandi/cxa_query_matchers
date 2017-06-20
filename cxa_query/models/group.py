from django.db import models
from cxa_query.models import *

class Group (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=False)
	category = models.CharField(max_length=1000, blank=True, null=True)
	eligibility = models.CharField(max_length=1000, blank=True, null=True)
	area_coverage = models.CharField(max_length=1000, blank=True, null=True)
	basic_coverage = models.CharField(max_length=1000, blank=True, null=True)
	list_desc = models.CharField(max_length=1000, blank=True, null=True)
	claim_procedure = models.CharField(max_length=1000, blank=True, null=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.name