from django import forms
from .models import Poll


class PollForm(forms.ModelForm):

# https://stackoverflow.com/questions/25223409/filtering-cities-by-country-in-the-django-admin-edit-form

    class Meta:
        model = Poll
        fields = '__all__'
