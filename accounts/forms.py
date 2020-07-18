from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required= True)
    last_name = forms.CharField(max_length= 100,required= True)
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = (
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2'
        )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None