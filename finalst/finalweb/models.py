from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Quote(models.Model):
	quote = models.CharField(max_length=300, null=True, blank=True)
	quote_author = models.CharField(max_length=30, null=True, blank=True)

	def __unicode__(self):
		return smart_unicode(self.quote)


class Project(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	location = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)
	complexity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])

	def __unicode__(self):
		return smart_unicode(self.name)


class Reference(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.CharField(max_length=1000, null=True, blank=True)
	image = models.CharField(max_length=30, null=False, blank=False)
	file = models.ImageField(upload_to = '', null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.name)


