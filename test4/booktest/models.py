from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length='20')
    bpub_date = models.DateField(db_column='pub_date')

    class Meta:
        db_table = 'bookinfo'

