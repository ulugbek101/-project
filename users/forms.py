from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileEdirForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['username', 'location', 'email', 'short_intro',
                  'bio', 'image', 'social_github', 'social_twitter',
                  'social_linkedin', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileEdirForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})