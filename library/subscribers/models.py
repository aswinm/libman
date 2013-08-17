from django.db import models

class Subscriber(models.Model):
	sid = models.CharField(max_length = 10 , primary_key = True)
	name = models.CharField(max_length = 100)
	gender =  models.CharField(max_length = 1)
	contact = models.CharField(max_length = 11)
	mail = models.EmailField(max_length = 30)
	NoOfBooks = models.IntegerField()

# Create your models here.
