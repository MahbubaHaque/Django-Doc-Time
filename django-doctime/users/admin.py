from django.contrib import admin
from users.models import Profile

admin.site.site_title = "Online Doctor solution"
admin.site.site_header = "Doctime"

admin.site.register(Profile)