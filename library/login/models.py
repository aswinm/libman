from django.db import models

class Auth(models.Model):
	username=models.CharField(max_length=200)
	passwd=models.CharField(max_length=20)
	def __unicode__(self):
		return self.username
# Create your models here.
