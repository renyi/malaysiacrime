from django.contrib import admin

from models import Moniton


class MonitonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Moniton, MonitonAdmin)
