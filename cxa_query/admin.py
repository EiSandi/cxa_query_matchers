from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Group)
admin.site.register(Benefits)
admin.site.register(Admission)
admin.site.register(Hospital)