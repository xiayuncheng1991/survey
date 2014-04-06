import datetime
import os

import Image
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.forms.models import ModelForm
from django.utils import timezone

from survey.settings import MEDIA_ROOT


# Create your models here.
IMAGE_PATH = "stationary/original"
THUMB_PATH = "stationary/thumb"

class StationaryType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=IMAGE_PATH)
    thumb = models.ImageField(upload_to=THUMB_PATH, blank=True)
    details = models.CharField(max_length=100, default='None')
    quantity_max=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
    def sum(self):
        num = 0
        for choice in self.choice_set.all():
            num = num + choice.num
        return num

    def save(self):
        super(StationaryType, self).save() 
        base, ext = os.path.splitext(os.path.basename(self.image.path))
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.image.path).replace('\\', '/'))
        relate_thumb_path = os.path.join(THUMB_PATH, base + '.thumb' + ext)
        thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path).replace('\\', '/')
        thumb_pixbuf.save(thumb_path)
        self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
        super(StationaryType, self).save()
        

    
class Choice(models.Model):
    user = models.ForeignKey(User)
    stationary_type = models.ForeignKey(StationaryType)
    num = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.user)

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ('num',)  
  
def make_thumb(path, size=96):
    pixbuf = Image.open(path)
    width, height = pixbuf.size
  
    if width > size: 
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)
        return pixbuf  
