
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'image'], name="unique_like"),
        ]
class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption','name']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        
        fields=['content']
        widgets= {
            'content':forms.Textarea(attrs={'rows':2,})
        }
