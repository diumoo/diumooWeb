from django.db import models
from sparkle.models import Application

class Feature(models.Model):
    content = models.TextField()
    rank = models.IntegerField(default=0)
    new = models.BooleanField(default=True)
    def __unicode__(self):
        return self.content
class Notice(models.Model):
    content = models.TextField()
    rank = models.IntegerField(default=0)
    important = models.BooleanField(default=False)
    def __unicode__(self):
        return self.content

class Sponsor(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class SponsorCate(models.Model):
    name = models.CharField(max_length=20)
    sponsors = models.ManyToManyField(Sponsor)
    rank = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Link(models.Model):
    url = models.URLField(verify_exists=False, max_length=200)
    title = models.CharField(max_length=140)
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return self.url

class ScreenShot(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to="static/images/", max_length=100)
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return self.image
class QA(models.Model):
    question = models.CharField(max_length=140)
    answer = models.TextField()
    def __unicode__(self):
        return self.question


