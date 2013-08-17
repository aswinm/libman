from django.db import models

class Book(models.Model):
	bid = models.CharField(primary_key = True, max_length = 20 )
	name = models.CharField(max_length = 100)
	author = models.CharField(max_length = 30)
	Totbooks = models.IntegerField()
	Avlbooks = models.IntegerField()

# Create your models here.
