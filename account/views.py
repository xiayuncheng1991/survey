from django.contrib.auth import authenticate,login as user_login, logout as user_logout 
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from account.models import UserForm


# Create your views here.
# coding=utf-8 
def index(request):
    form=UserForm()  
    return render(request, 'account/login.html',{'form':form})  

def login(request):
    form=UserForm()  
    if request.user.is_authenticated():  
        return  HttpResponse('You are logining!')  
    if request.method == 'POST':
        form = UserForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        else:
            username = " "
            password = " "
        user = authenticate(username=username, password=password)  
        if user is not None:  
            if user.is_active:  
                        user_login(request, user)  
#                         return HttpResponseRedirect('/account/%d' % user.id)  
                        return HttpResponseRedirect(reverse('stationary:index'))
            else:  
                    return render(request, 'account/login.html', {'error_message': "This username has not been registered!",'form':form,})
        else:  
                return render(request, 'account/login.html', {'error_message': "The username or password is wrong!",'form':form})  
    else:    
        return render(request,'account/login.html',{'error_message': "Please login first!",'form':form})

def logout(request):  
    user_logout(request)
    form=UserForm()   
    return render(request,'account/login.html',{'form':form,})  