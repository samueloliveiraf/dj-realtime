from django import forms

from notify.models import Notification


class CarForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
