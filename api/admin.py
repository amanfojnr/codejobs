from django.contrib import admin
from .models import Listing, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Listing)
