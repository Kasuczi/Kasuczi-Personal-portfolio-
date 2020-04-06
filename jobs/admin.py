from django.contrib import admin
from .models import Job

# admin registers a class of Job created in views
admin.site.register(Job)