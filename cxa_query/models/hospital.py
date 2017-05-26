from django.db import models

class Hospital (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=False)
	details = models.CharField(max_length=500, blank=True, null=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.name