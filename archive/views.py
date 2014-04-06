from datetime import date

from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from archive.models import DateArchive, StationaryArchive
from stationary.models import StationaryType


# Create your views here.
def stationary_index(request):
    if request.method == "POST":
        return archive_stationary(request)
    else:    
        stationary_archive_list = StationaryArchive.objects.all()
        return render(request, "archive/stationary_archive.html", {"stationary_archive_list":stationary_archive_list, })

def archive_stationary(request):
    user_list = User.objects.all()
    stationary_list = StationaryType.objects.all()
    if not DateArchive.objects.filter(year=date.today().year, month=date.today().month):
        date_archive = DateArchive(year=date.today().year, month=date.today().month)
        date_archive.save()
        for user in user_list:
            for stationary in stationary_list:
                choice = user.choice_set.get(stationary_type=stationary)
                date_archive.stationaryarchive_set.create(email=user.email, username=user.username, stationaryname=stationary.name, num=int(choice.num)) 
                choice.delete()
        return HttpResponseRedirect(reverse('archive:stationary_archive_index'))
    else:
        return HttpResponse("You already archive in this month!")
        
def get_stationaryarchive_json(request):
    data = serializers.serialize('json', StationaryArchive.objects.all(), ensure_ascii = False,use_natural_keys=True)
    return HttpResponse(data, content_type='json')