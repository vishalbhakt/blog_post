from django.contrib import admin
from . models import Post,CustomUser,ProfileUpdate

# Register your models here.

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(ProfileUpdate)