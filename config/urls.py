"""Cbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 


from workflows.accounts_workflows import (
                                            createUserProfile,
                                            userLogin,
                                            updateUserProfile,
                                            userPasswordReset,
                                            deleteUserProfile
                                         )


from workflows.ewallet_workflows import (
                                            getUserBalance,
                                            addMoneytoAccount,
                                            sendMoneytoUser
                                        )


urlpatterns = [
    path('admin/', admin.site.urls),

    #Account url's
    path('signup/', createUserProfile,name='createUser'),
    path('login/',userLogin,name='userlogin'),
    path('update/<int:userID>/',updateUserProfile, name='updateuser'),
    path('resetpassword/',userPasswordReset,name='resetpassword'),
    path('deleteuser/<int:userID>',deleteUserProfile,name="deleteuser"),

    #ewallet url's
    path('',getUserBalance,name='getbalance'),
    path('addmoney/',addMoneytoAccount,name='addmoney'),
    path('sendmoney/',sendMoneytoUser, name = 'sendmoney')   

]
