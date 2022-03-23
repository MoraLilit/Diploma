from DD.models import User, Subjects, Groups, Theory
from django.forms import forms


class ProfilePic(forms.Form):
    class Meta:
        model = User
        fields = 'photo'
