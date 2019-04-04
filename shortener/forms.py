from django import forms

from shortener.models import Shortcut


class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ['url']
