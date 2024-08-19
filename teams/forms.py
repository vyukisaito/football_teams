from django import forms
from teams.models import Team


class TeamsForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
