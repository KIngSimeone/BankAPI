from .models import Transaction, Account
import random

import string

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def createUserAccount(user):
    try:
        if user is None:
            return None

        useraccount = Account(user=user)
        useraccount.accountnumber = user.phone
        useraccount.balance = 0

        useraccount.save()

        return useraccount

    except Exception as e:
        logger.error("createuseraccount@Error")
        logger.error(e)

def createTransactionRecord(user,account,transType,desc):
    try:
        if user is None:
            return None
        N = 15
        ref_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

        trans = Transaction(user=user, account=account, transType=transType, desc=desc)
        print(trans.transType)
        trans.refId = ref_id

        trans.save()
    except Exception as e:
        logger.error("createTransactionRecord@Error")
        logger.error(e)

    return trans




