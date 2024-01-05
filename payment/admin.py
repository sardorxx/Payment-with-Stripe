from django.contrib import admin

# Register your models here.


from .models import Tax, Item, Discount, Order

admin.site.register([Tax, Item, Discount, Order])
