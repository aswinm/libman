from django.db import models

class LendBook(models.Model):
        tid = models.AutoField(primary_key = True)
	bid = models.ForeignKey('books.Book')
	sid = models.ForeignKey('subscribers.Subscriber')
	date = models.DateField()


# Create your models here.
