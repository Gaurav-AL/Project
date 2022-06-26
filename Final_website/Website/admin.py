from django.contrib import admin

# Register your models here.
from Website.models import userDetail,contactsInfo,billInfo



admin.site.register(userDetail)
admin.site.register(contactsInfo)
admin.site.register(billInfo)
