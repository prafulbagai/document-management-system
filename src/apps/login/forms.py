from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import UserProfile

class DocumentForm(forms.Form):
    
    docfile = forms.FileField(
        label='Select a file',
        
    )
    
class RegisterForm(UserCreationForm):
    gender= forms.ChoiceField(choices=UserProfile.GENDER)
    
    def save(self, *args, **kwargs):
        user = super(RegisterForm,self).save(*args,**kwargs)
        
        UserProfile.objects.create(user=user , gender=self.cleaned_data['gender'])
        
        return user
