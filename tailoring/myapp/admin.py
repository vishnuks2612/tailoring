from django.contrib import admin

# Register your models here.
from .models import user_login, user_details, Product, purchase, Category, Feedback
from . models import *

admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(Product)
admin.site.register(purchase)
admin.site.register(Feedback)



class Cat_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
admin.site.register(Category, Cat_admin)