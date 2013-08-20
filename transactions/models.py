from django.db import models

class LendBook(models.Model):
        tid = models.AutoField(primary_key = True)
	bid = models.ForeignKey('books.Book',to_field = 'bid')
	sid = models.ForeignKey('subscribers.Subscriber', to_field = 'sid')
	date = models.DateField()
	returned  = models.BooleanField()



# Create your models here.
