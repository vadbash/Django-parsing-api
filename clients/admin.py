from django.contrib import admin
from .models import ClientsList, NoActiveClientsList, NotActivePositiveBalance


class ClientsListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'current_balance', 'status', 'reg_date')

class NoActiveClientListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'current_balance', 'status', 'lastcall_date')

class NotActivePositiveBalanceAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'current_balance', 'status', 'reg_date')


admin.site.register(ClientsList, ClientsListAdmin)
admin.site.register(NoActiveClientsList, NoActiveClientListAdmin)
admin.site.register(NotActivePositiveBalance, NotActivePositiveBalanceAdmin)