from django.contrib import admin

# Register your models here.
from grocery_list.models import GroceryList

admin.site.register(GroceryList)
