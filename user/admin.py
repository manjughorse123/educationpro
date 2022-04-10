from django.contrib import admin
from user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('email',)}
    list_display = ('first_name', 'email')


admin.site.register(User,UserAdmin)

