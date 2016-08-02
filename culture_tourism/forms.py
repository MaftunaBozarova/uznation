from django import forms
from .models import Feedback
from redactor.widgets import RedactorEditor


class FeedBackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'usr',
        'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'email', 'placeholder': 'Email'}))
    comment = forms.CharField(widget=RedactorEditor(attrs={'placeholder': 'Comment'}))

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='', max_length=512, required=False, widget=forms.TextInput(attrs={'type': 'search', 'name': 'search-word', 'placeholder': 'Search'}))
