from django.contrib.auth.hashers import make_password, check_password
import secrets 

from .models import (
                    User,
                    HomeAddress,
                    UserAccessTokens, 
                    UserPasswordResetTokens
                    )

from django.utils import timezone

from datetime import datetime,timedelta
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

def authenticateUser(email,password):
    try:

        user = User.objects.get(email__iexact=email)

        if check_password(password, user.password):
            user.lastActiveOn = timezone.now()

            user.save()
            return user

        return None
        
    except Exception as e:
        logger.error("authenticateUser@Error")
        logger.error(e)
        return None


def generateUserAccessToken(user):
    try:
        if user is None:
            return None

        userAccessTokenRecords = UserAccessTokens.objects.filter(user=user.id)
        
        userAccessTokenRecord = None
        if len(userAccessTokenRecords) > 0:
            userAccessTokenRecord = userAccessTokenRecords[0]
            if userAccessTokenRecord.expiresAt > timezone.now():

                return userAccessTokenRecord
        
        else:
            userAccessTokenRecord = UserAccessTokens(user=user)
            
        userAccessTokenRecord.accessToken = secrets.token_urlsafe()

        userAccessTokenRecord.expiresAt = getExpiresAt()

        userAccessTokenRecord.save()

        return userAccessTokenRecord

    except Exception as e:
        logger.error("generteUserAccessToken@Error")
        logger.error(e)
        return None

def createUserAddress(user,street,city,state,country,zipcode):
    try:
        if user is None:
            return None

        useraddress = HomeAddress(user=user)
        useraddress.street = street
        useraddress.city = city
        useraddress.state = state
        useraddress.country = country
        useraddress.zipCode = zipcode

        useraddress.save()

        return useraddress

    except Exception as e:
        logger.error("createuseraddress@Error")
        logger.error(e)

def getUserByAccessToken(accessToken):
    try:
        userAccessTokenRecord = UserAccessTokens.objects.filter(
            accessToken=accessToken)
        if len(userAccessTokenRecord) > 0:
            userAccessTokenRecord = userAccessTokenRecord[0]
            if userAccessTokenRecord.expiresAt > timezone.now():
                associatedUser = userAccessTokenRecord.user
                if not associatedUser is None and userAccessTokenRecord.expiresAt > timezone.now():

                    associatedUser.lastActiveOn = timezone.now()
                    userAccessTokenRecord.expiresAt = getLastActiveForwarding()

                    userAccessTokenRecord.save()
                    associatedUser.save()

                    return userAccessTokenRecord.user

            return None
        else:
            return None

        return None
    except UserAccessTokens.DoesNotExist:
        print('getUserByAccessToken@Error')
        return None

def updateUser(user, firstName, lastName, userName, email, phone,password=None):
    try:
        user.firstName = firstName
        user.lastName = lastName
        user.userName = userName
        user.email = email
        user.phone = phone

        if password:
            hashedPassword = make_password(password)
            user.password = hashedPassword

        user.save()
        return user

    except Exception as e:
        logger.error('updateUser@error')
        logger.error(e)
        return None


def getUserByID(userId):
    try:
        return User.objects.get(id=userId)

    except Exception as e:
        logger.error('getUserById@error')
        logger.error(e)
        return None

def deleteUser(user):
    try:
        user.isDeleted = True
        user.save()

        return user
    except Exception as e:
        logger.error('deleteUser@error')
        logger.error(e)
        return None

def resetPassword(user,password):
    try:
        hashedPassword = make_password(password)
        user.password = hashedPassword

        user.save()
        return True
    except Exception as e:
        logger.error('resetPassword@error')
        logger.error(e)
        return False


def getUserPasswordResetTokenByResetToken(passwordResetToken):
    try:
        userPasswordTokenRecord = UserPasswordResetTokens.objects.filter(
            resetToken=passwordResetToken)
        if len(userPasswordTokenRecord) > 0:
            userPasswordTokenRecord = userPasswordTokenRecord[0]
            currentDateTime = datetime.now().date()
            if currentDateTime <= userPasswordTokenRecord.expiresAt:
                return userPasswordTokenRecord

            return None

        return None
    except UserPasswordResetTokens.DoesNotExist:
        logger.error('getUserByPasswordResetToken@Error')
        # logger.error(e)
        return None

def getExpiresAt():
    return (timezone.now() + timedelta(minutes=eval(settings.DURATION)))

def getLastActiveForwarding():
    return (timezone.now() + timedelta(minutes=eval(settings.DURATION)))



