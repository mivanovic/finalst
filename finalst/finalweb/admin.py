from django.contrib import admin

# Register your models here.

from finalweb.models import Quote, Project, Reference

class QuoteAdmin(admin.ModelAdmin):
	class Meta:
		model = Quote

class ProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = Project

class ReferenceAdmin(admin.ModelAdmin):
	class Meta:
		model = Reference


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Reference, ReferenceAdmin)