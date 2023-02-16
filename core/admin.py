from django.contrib import admin
from core.models import Sessao, Produto

# Register your models here.

class EventoAdmin (admin.ModelAdmin):
    list_filter = ('sessao',)

admin.site.register (Sessao)
admin.site.register (Produto, EventoAdmin)
