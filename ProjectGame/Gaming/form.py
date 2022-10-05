from django import forms
from .models import Game

class gameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"