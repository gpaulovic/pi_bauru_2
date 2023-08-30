from django.contrib import admin
from .models import Descartadores

class DescartadoresAdmin(admin.ModelAdmin):
    list_display = ['nome', 'documento', 'email', 'endereco']
    search_fields = ['nome', 'documento', 'email', 'endereco']

admin.site.register(Descartadores, DescartadoresAdmin)
