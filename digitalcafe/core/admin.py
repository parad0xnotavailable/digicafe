from django.contrib import admin

from .models import Product
from .models import CartItem
from .models import Transaction
from .models import LineItem

# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Transaction)
admin.site.register(LineItem)