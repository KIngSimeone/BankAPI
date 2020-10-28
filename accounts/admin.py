from django.contrib import admin
from .models import (
                    User,
                    HomeAddress,
                    UserAccessTokens
                    )

admin.site.register(User)
admin.site.register(HomeAddress)
admin.site.register(UserAccessTokens)
