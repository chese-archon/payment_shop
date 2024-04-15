from django.contrib import admin
from .models import Customer, OrderItem

admin.site.register(OrderItem)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city',
                    'created', 'updated']
    list_filter = ['created', 'updated']