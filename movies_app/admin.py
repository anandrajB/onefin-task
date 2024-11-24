from django.contrib import admin

from .models import Collections, Genre, Movies

admin.site.site_title = "OneFin Task Admin Panel"
admin.site.site_header = "OneFin Task"
admin.site.register(Movies)
admin.site.register(Collections)
admin.site.register(Genre)
