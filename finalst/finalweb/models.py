from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import MaxValueValidator, MinValueValidator


class Quote(models.Model):
    quote = models.CharField(max_length=300, null=True, blank=True)
    quote_author = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.quote)


class Reference(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.CharField(max_length=100, null=True, blank=True)
    complexity = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(99)])

    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    time = models.CharField(max_length=1000, null=True, blank=True)
    customer = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class RefImages(models.Model):
    reference = models.ForeignKey(Reference)
    file = models.ImageField(upload_to='', null=True, blank=True)



