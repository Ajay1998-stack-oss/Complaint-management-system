from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Manager)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Complaint)
admin.site.register(Feedback)