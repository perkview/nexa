from django.contrib import admin
from .models import ContactMessage, BusinessChallenge

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(BusinessChallenge)