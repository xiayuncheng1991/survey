from django.db import models

# Create your models here.

class DateArchive(models.Model):
    year=models.CharField(max_length=10)
    month=models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.year+"-"+self.month
    def natural_key(self):
        return (self.year, self.month)
    
class StationaryArchive(models.Model):
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    stationaryname = models.CharField(max_length=100)
    num=models.IntegerField(default=0)
    date=models.ForeignKey(DateArchive)
    
    def __unicode__(self):
        return self.email