from django import forms
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserStatistics(User):
    class Meta:
        proxy=True
        ordering = ('id',) 
    def get_groupname(self):
        group_list=self.groups.all()
        return group_list[0]
#     get_groupname.admin_order_field = 'first_name'
    get_groupname.short_description = 'Which groups?'

class UserForm(forms.Form):
    username =  forms.CharField(required=True,  
        label=u"Username",  
        error_messages={'required': u'Pleasr input username'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"username",  
            }  
        ),  )
    password =  forms.CharField(required=True,  
        label=u"Password",  
        error_messages={'required': u'Pleasr input password'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }  
        ),  )