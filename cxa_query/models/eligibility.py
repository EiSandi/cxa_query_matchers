from django.db import models

class Eligibility (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=500, blank=False)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.description