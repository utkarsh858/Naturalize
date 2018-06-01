from django.db import models

# Create your models here.
class Citizen(models.Model):
	"""docstring for MainModel"""
	aadhar_number = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	points = models.CharField(max_length=10)