from django.http import JsonResponse, HttpResponse
from ewallet.models import Account
from accounts.models import User
from accounts.views import getUserByAccessToken
from ewallet.views import createTransactionRecord


import json

import logging

logger = logging.getLogger(__name__)


def getUserBalance(request):

    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)
    
    if user is None:
        return HttpResponse('User Authentication Failed')
    
    account = Account.objects.get(user=user)
    data = {"balance":account.balance}

    return JsonResponse(data)

def addMoneytoAccount(request):
    if request.method == 'POST':
        try:
            token = request.headers.get('accessToken')
            user = getUserByAccessToken(token)

            if user is None:
                return HttpResponse('User Authentication Failed')
                
            data = json.loads(request.body)
            amount = data['amount']
            transType = data['transtype']
            desc = data['desc']

            account = Account.objects.get(user=user)
           
            account.balance = int(amount)+ account.balance
            
            account.save()
            print(account.balance)

            createtransaction=createTransactionRecord(user,account,transType,desc)
            
            return HttpResponse("Transaction Successful")
        except Exception as e:
            logger.error("addmoney@Error")
            logger.error(e)

def sendMoneytoUser(request):
    if request.method == 'POST':
        try:
            token = request.headers.get('accessToken')
            user = getUserByAccessToken(token)

            data = json.loads(request.body)
            phone = data['phone_no']
            amount = data['amount']
            transType = data['transtype']
            desc = data['desc']


            receiverUser=User.objects.filter(phone=phone)
            print(receiverUser)
            receiverUser = receiverUser[0]
            print(receiverUser)
            print(user)

            sender = Account.objects.get(user=user)
            print(sender)
            receiver = Account.objects.get(user=receiverUser)

            sender.balance = sender.balance - int(amount)
            receiver.balance = receiver.balance + int(amount)
            print(sender.balance)
            print(receiver.balance)

          

            sender.save()
            receiver.save()

            account=sender

            createtransaction=createTransactionRecord(user,account,transType,desc)

            return HttpResponse("Transaction Succesful")

        except Exception as e:
            logger.error("SendMoneyerror@Error")
            logger.error(e)
            

