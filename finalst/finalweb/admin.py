from django.contrib import admin

# Register your models here.

from finalweb.models import Quote, Project, Service

class QuoteAdmin(admin.ModelAdmin):
	class Meta:
		model = Quote

class ProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = Project

class ServiceAdmin(admin.ModelAdmin):
	class Meta:
		model = Service


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)