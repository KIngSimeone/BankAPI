from django.db import models
from django.utils.timezone import now


#User Model
class User(models.Model):
    firstName = models.TextField("first_name")
    lastName = models.TextField("last_name")
    userName = models.TextField("user_name")
    email = models.EmailField(max_length=254)
    password = models.TextField()
    phone = models.TextField()

    isDeleted = models.BooleanField("is_deleted", default=False)
    createdAt = models.DateField("created_at", auto_now_add=True)
    updatedAt = models.DateField("updated_at", auto_now=True)

    isActive = models.BooleanField("is_active", default=True)
    lastActiveOn = models.DateTimeField("last_active_on", default=now)

    def __str__(self):
        fullName = self.firstName + " " + self.lastName + str(self.id)
        return fullName

    class Meta:
        ordering = ['id']

#UseraddressModel
class HomeAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    street = models.TextField(null=False)
    city = models.CharField(max_length=64, null=False)
    state = models.CharField(max_length=64, null=False)
    country = models.CharField(max_length=64, null=False)
    zipCode = models.CharField(max_length=64, null=False)

    
    def __str__(self):
        address = str(self.user) +"'s Address"
        return address



#useraccesstoken
class UserAccessTokens(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    accessToken = models.TextField("access_token")

    expiresAt = models.DateTimeField("expires_at")
    createdAt = models.DateTimeField("created_at", auto_now_add = True)
    updatedAt = models.DateTimeField("updated_at",auto_now= True)

    class Meta :
        verbose_name = "User Access Token"
        verbose_name_plural ="User Access Tokens"

    def __str__(self):
        token = str(self.user) +"'s Token"
        return token

#resettokenmodels
class UserPasswordResetTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    resetToken =  models.TextField("reset_token")

    expires_at = models.DateField("expires_at")
    createdAt = models.DateField("created_at",auto_now_add=True)
    updated_at = models.DateField("updated_at", auto_now=True)

    