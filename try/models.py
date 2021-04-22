from django.db import models

# Create your models here.
class Customer(models.Model):
    emp_id = models.FloatField(primary_key=True)
    emp_name = models.CharField(unique=True, max_length=30)
    mobno = models.IntegerField(unique=True)
    emailid = models.CharField(max_length=30, blank=True, null=True)
    currentbal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer'

    
class Transfer(models.Model):
    emp_id = models.FloatField(blank=True, null=True)
    receiver = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    sender = models.CharField(max_length=30, blank=True, null=True)
    recname = models.CharField(max_length=30, blank=True, null=True)
    updabalofsender = models.IntegerField(blank=True, null=True)
    transid = models.IntegerField(primary_key=True)
    class Meta:
        managed = True 
        db_table = 'transfer'