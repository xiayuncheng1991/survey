import re

from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import stationary
from stationary.models import StationaryType


# Create your views here.
def index(request):
    if request.method == "POST": 
        return submit(request)
    else:
        context = {'user':request.user, 'stationary_list':StationaryType.objects.all(),}
        return render(request, 'stationary/index.html', context)

def result(request):
    return render(request, 'stationary/result.html', {'user_list':User.objects.all(), 'stationary_list':StationaryType.objects.all()})


def submit(request):
    u = request.user
    if  u.is_anonymous():
        return HttpResponseRedirect(reverse('account:login'))
    try:
        stationary_list = StationaryType.objects.all()
    except(KeyError, StationaryType.DoesNotExist):
        return render(request, 'stationary/index.html', {
            'error_message': "You did a illegal operation!",
           })
    else:
        num_list = ["1"]
        pattern = re.compile(u"^[1-9]\d{1,2}$|^[0-9]$")
        for stationary in stationary_list:
            num = request.POST[stationary.name+str(stationary.id)]
            if not pattern.search(num) or int(num) > stationary.quantity_max :
                return render(request, 'stationary/index.html', {'error_message': "You didn't input right numbers.", 'stationary_list':StationaryType.objects.all(), })
            else:
                num_list.append(num)
        i = 0
        for stationary in stationary_list:   
            c = u.choice_set.filter(stationary_type=stationary)
            if c:
                c.delete() 
            u.choice_set.create(stationary_type=stationary, num=int(num_list[i]))
            i = i + 1    
        return HttpResponseRedirect(reverse('stationary:result'))

    
def get_stationarytype_json(request):
    data = serializers.serialize('json', StationaryType.objects.all(), ensure_ascii = False)
    return HttpResponse(data, content_type='json')
#     return  HttpResponse(json.dumps(data,ensure_ascii = False),content_type='json')
