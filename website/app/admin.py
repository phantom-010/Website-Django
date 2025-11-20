from django.contrib import admin
from .models import *
from .models import Contract
# Register your models here.
admin.site.register(Person)
admin.site.register(Contract)
admin.site.register(Taskadd)