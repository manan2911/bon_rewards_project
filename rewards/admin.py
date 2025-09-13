from django.contrib import admin
from .models import User, Bill, Reward

admin.site.register(User)
admin.site.register(Bill)
admin.site.register(Reward)
