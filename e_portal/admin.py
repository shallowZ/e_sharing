from django.contrib import admin
from .models import Customers, Operators, Vehicles, OperationsHistory, Payments, RepairHistory

# Register your models here.
admin.site.register(Customers)
admin.site.register(Operators)
admin.site.register(Vehicles)
admin.site.register(OperationsHistory)
admin.site.register(Payments)
# admin.site.register(TopUpHistory)
admin.site.register(RepairHistory)
