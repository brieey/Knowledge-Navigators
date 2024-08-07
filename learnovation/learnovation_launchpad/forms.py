from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
 
 
class SignUpForm(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Enter your name', 
            'maxlength': '16', 
            'minlength': '6', 
            })
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'@email.com', 
            'maxlength': '100', 
            'minlength': '6', 
            })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input', 
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'placeholder':'Create password',
            'maxlength': '22',
            'minlength': '8',
            })
        del self.fields['password2']

    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1')
        
    