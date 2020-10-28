import json

from django.http import HttpResponse

from accounts.models import (
                             User,
                             HomeAddress,
                             UserAccessTokens,
                             UserPasswordResetTokens
                            )

from accounts.views import (
                            authenticateUser, 
                            generateUserAccessToken,
                            getUserByAccessToken,
                            updateUser,
                            deleteUser,
                            getUserByID,
                            resetPassword,
                            createUserAddress,
                            getUserPasswordResetTokenByResetToken,
                            getExpiresAt,
                            getLastActiveForwarding,
                            )

from ewallet.views import createUserAccount

from django.contrib.auth.hashers import make_password, check_password


def createUserProfile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        firstname = data['firstname']
        lastname =  data['lastname']
        username = data['username']
        email = data['email']
        phone = data['phone']
        password = data['password']
        street = data['street']
        city = data['city']
        state = data['state']
        country = data['country']
        zipcode = data['zipcode']

        hashed_password = make_password(password)
       
        home = HomeAddress()
        profile = User()

        profile.firstName = firstname
        profile.lastName = lastname
        profile.userName = username
        profile.email = email
        profile.phone = phone
        profile.password = hashed_password

        profile.save()

        user = authenticateUser(email, password)

        userAccessToken = generateUserAccessToken(user)

        userAddress = createUserAddress(user,street=street,city=city,state=state,country=country,zipcode=zipcode)
        userAccount = createUserAccount(user)

        return HttpResponse("User Succesfully created")


def userLogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password =  data['password']

        user = authenticateUser(email, password)
        print('Hi there here i am',user)


        if user is None:
            return HttpResponse("Invalid credentials")

        userAccessToken = generateUserAccessToken(user)
        
        return HttpResponse("Login Successful")

def updateUserProfile(request, userID):

    data = json.loads(request.body)
    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)
    
    if user is None:
        return HttpResponse("User Authentication Failed")

    if 'password' in data:
        keys = ['email', 'username', 'firstname',
                'lastname','phone','password']

    else:
        keys = ['email', 'username', 'firstname',
                'lastname', 'phone'] 

    #check if user already exists
    userToBeUpdated = getUserByID(userID)
    if  userToBeUpdated is None:
        return HttpResponse('User does not exist')

    if 'password' in data:
        updatedUser = updateUser(userToBeUpdated, firstName=data['firstname'],
                                lastName=data['lastname'], userName=data['username'],
                                email=data['email'], password=data['password'], phone=data['phone']
                                )

    else:
        updatedUser = updateUser(userToBeUpdated, firstName=data['firstname'],
        lastName=data['lastname'], userName=data['username'],
        email=data['email'], phone=data['phone']
        )

    if updateUser == None:
        return HttpResponse("Invalid User")

    return HttpResponse("User successfully updated")

def deleteUserProfile(request,userID):
    if request.method == 'DELETE':
        token = request.headers.get('accessToken')
        user = getUserByAccessToken(token)

        if user is None:
            return HttpResponse("User Authentication Failed")
        
        userToBeDeleted = getUserByID(userID)
        if userToBeDeleted == None:
            return HttpResponse("User Authentication Failed")

        userDeleted = deleteUser(userToBeDeleted)
        if userDeleted is None:
            return HttpResponse("Invalid User")

        return HttpResponse("User Successfully deleted")


def userPasswordReset(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        userPasswordResetToken = getUserPasswordResetTokenByResetToken(data['token'])
        
        if userPasswordResetToken is None:
            return HttpResponse("I ncorrect Token")

        password = data['password']

        userPasswordReset = resetPassword(userPasswordResetToken.user, password)
        if userPasswordReset == False:
            return HttpResponse("User password reset failed")

        return HttpResponse("Password reset succesful")


def verifyToken(request):

    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)

    if user is None:
        return HttpResponse("Unauthorised User")

    return HttpResponse("Token is Valid")

