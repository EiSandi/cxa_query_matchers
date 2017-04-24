from django.db import models
from cxa_query.models import *

class Group (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=False)
	group_eligibility = models.OneToOneField(Eligibility, default="", blank=True, null=True)
	group_area_coverage = models.ForeignKey(AreaCoverage, default="", blank=True, null=True)
	group_basic_coverage = models.ForeignKey(BasicCoverage, default="", blank=True, null=True)
	category = models.CharField(max_length=100, blank=False, null=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.name