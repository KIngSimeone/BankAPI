from django.db import models
from django.utils.timezone import now
from accounts.models import User

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accountnumber = models.TextField(max_length=20)
    balance = models.IntegerField(default=0)

    isDeleted = models.BooleanField("is_deleted", default= False)
    createdAt = models.DateField("created_at", auto_now_add=True)
    updatedAt = models.DateField("updated_at", auto_now=True)

    def __str__(self):
        accbal = str(self.user) + "'s Account"
        return accbal


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    refId = models.TextField(max_length=15)
    transType = models.TextField(max_length=64, null=False)

    desc = models.TextField(max_length=254, null= True)
    
    createdAt = models.DateField("created_at", auto_now_add=True)
    updatedAt = models.DateField("updated_at",auto_now=True)

    def __str__(self):
        refid = self.refId
        return refid

