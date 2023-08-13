from django.contrib import admin

# Register your models here.
from .models import Ticket,Customer

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'service',
                    'details',
                    'assigned_to',
                    'created',
                    'updated',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'dob','address','city','pincode','gender','customer_id',)
# Register Models
admin.site.register(Ticket, TicketAdmin)

admin.site.register(Customer)

