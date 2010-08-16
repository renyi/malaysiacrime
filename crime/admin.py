from django.contrib import admin

from models import Crime


class CrimeAdmin(admin.ModelAdmin):
    list_filter   = ('date', 'updated_at')
    ordering      = ('-created_at',)
    list_display  = ('headline', 'author', 'date', 'created_at', 'is_removed')
    search_fields = ('headline',)
admin.site.register(Crime, CrimeAdmin)
