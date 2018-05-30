from django.db import models

# Create your models here.
class MainModel(models.Model):
	"""docstring for MainModel"""
	def __init__(self, arg):
		super(MainModel, self).__init__()
		self.arg = arg
		
	aadhar_number = models.CharField(max_length=200)
	password = models.CharField(max_length=200)