from django.contrib import admin
from finalweb.models import Quote, Reference


class QuoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Quote


class ReferenceAdmin(admin.ModelAdmin):
    class Meta:
        model = Reference

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Reference, ReferenceAdmin)