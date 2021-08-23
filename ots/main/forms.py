from django import forms
from .models import balaka, RATE_CHOICES


class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget= forms.Select(), required=True)

    class Meta:
        model = balaka
        fields = ('text', 'rate')
