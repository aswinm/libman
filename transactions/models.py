from django.db import models

class LendBook(models.Model):
        tid = models.AutoField(primary_key = True)
	bid = models.ForeignKey('books.Book',to_field = 'bid')
	sid = models.ForeignKey('subscribers.Subscriber', to_field = 'sid')
	date = models.DateField()
	DueDate = models.DateField()
	returned  = models.BooleanField()
	ReturnDate = models.DateField(null = True)



# Create your models here.
