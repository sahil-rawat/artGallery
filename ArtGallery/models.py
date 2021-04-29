from django.db import models
from django.forms.widgets import Widget


class Art(models.Model):
    arttype = (
        ('P', 'Painting'),
        ('S', 'Sketch'),
        ('O', 'Other'),
        ('N', 'None')
    )
    

    title = models.CharField(db_column='Title', max_length=30)
    arttype = models.CharField(choices=arttype, max_length=10, default="N")
    saleStatus = models.BooleanField(db_column='status')
    quantity = models.IntegerField(db_column='Quantity')
    date = models.DateField(db_column='Date') 
    price = models.FloatField(db_column='Price')
    desc = models.TextField(db_column='Description')
    artImg = models.ImageField(db_column='Art_Img',upload_to='')

    class Meta:
        db_table = 'Art'