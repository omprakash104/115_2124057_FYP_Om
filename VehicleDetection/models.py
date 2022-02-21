from django.db import models
from django.urls import reverse

# Create your models here.

class Review(models.Model):
	username = models.CharField(max_length = 300)
	email = models.CharField(max_length = 300)
	slug = models.CharField(max_length = 400)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add = True)