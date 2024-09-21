from django.contrib import admin
from .models import Project, Expertise, Certificate

# Register your models here.
admin.site.register(Project)
admin.site.register(Expertise)
admin.site.register(Certificate)