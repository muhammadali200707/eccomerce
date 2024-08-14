from django.contrib import admin
from django.contrib.auth.models import User, Group
from customer.models import Customer

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'address', 'phone')
    search_fields = ('full_name',)
    list_filter = ('first_name', 'last_name')
