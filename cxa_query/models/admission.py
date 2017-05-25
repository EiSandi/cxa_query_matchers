from django.db import models

class Admission (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=200, blank=False)
	before_admission = models.CharField(max_length=500, blank=False, null=True)
	upon_discharge = models.CharField(max_length=500, blank=False, null=True)
	after_discharge = models.CharField(max_length=500, blank=False, null=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.description