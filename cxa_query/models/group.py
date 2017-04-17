from django.db import models

class Group (models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=False)

	class Meta:
		ordering = ('created',)