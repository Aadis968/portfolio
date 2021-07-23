from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
]

# Django admin header customization
admin.site.site_header = "Log in to Developer Aaditya"
admin.site.site_title = "Welcome to Aaditya's Dashboard"
admin.site.index_title = "Welcome to the Admin Portal"