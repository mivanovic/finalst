from django.contrib import admin
from finalweb.models import Quote, Reference, RefImages


class QuoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Quote


class ImageInline(admin.TabularInline):
    model = RefImages


class ReferenceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Reference, ReferenceAdmin)