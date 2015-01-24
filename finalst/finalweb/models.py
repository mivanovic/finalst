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
    description = models.CharField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    file = models.ImageField(upload_to='', null=True, blank=True)
    complexity = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(99)])

    def __unicode__(self):
        return smart_unicode(self.name)


