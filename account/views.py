from django.contrib.auth import authenticate, login as user_login, logout as user_logout 
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


# Create your views here.
# coding=utf-8 
def login(request):  
    if request.user.is_authenticated():  
        return  HttpResponse('You are logining!') 
    if request.method == 'POST':
        if 'error_login' in request.session:
            del request.session['error_login']
        username = request.POST['username']  
        password = request.POST['password']
        user = authenticate(username=username, password=password)  
        if user is not None:  
            if user.is_active:  
                user_login(request, user)  
#                         return HttpResponseRedirect('/account/%d' % user.id)  
            else:  
                request.session['error_login'] = "This account is being used!"
        else:  
            request.session['error_login'] = "The username or password is wrong!"
    else:
        request.session['error_login'] = "Please login first!"   
    return HttpResponseRedirect(reverse(get_reverseurl_by_anonymity(request)))

def logout(request):
    reverse_url=get_reverseurl_by_anonymity(request)
    user_logout(request)
    return HttpResponseRedirect(reverse(reverse_url))

def get_errorlogin_session(request):
    if "error_login" in request.session:
        return request.session['error_login']
    else:
        return None
    
def set_reverseurl_by_anonymity(request, reverse_url):
    if "reverse_url" in request.session:
        del request.session['reverse_url']
    request.session['reverse_url'] = reverse_url
    
def get_reverseurl_by_anonymity(request):
    if "reverse_url" in request.session:
        return request.session['reverse_url']
    else:
        return "404.html"
