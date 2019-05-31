from django.contrib.gis.db import models

# Create your models here.
class Login(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=60)

	def __str__(self):
		return self.name



