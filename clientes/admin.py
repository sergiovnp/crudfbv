from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_per_page = 9
    search_fields = ('nombre', 'apellido')
    list_display = ('nombre', 'apellido', 'edad', 'dni', 'status')
    fields = ('nombre', 'apellido', 'edad', 'dni', 'status', 'created', 'updated')
    list_display_links =('apellido',)


admin.site.register(Cliente, ClienteAdmin)
