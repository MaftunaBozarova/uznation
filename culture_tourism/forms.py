from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'name': 'text-field-required','value':'', 'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required text-field-class wpcf7-use-title-as-watermark',
                                                         'size':'12', 'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'Emailfield', 'value': '', 'class': 'wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email email-class wpcf7-use-title-as-watermark',
                                                            'size': '12', 'placeholder':'Email'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'wpcf7-form-control wpcf7-textarea textarea-class wpcf7-use-title-as-watermark',
                                                           'rows':'9', 'cols':'39', 'placeholder': 'Your Comment'}))

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='', max_length=512, required=False, widget=forms.TextInput(attrs={'type': 'search', 'name': 'search-word', 'placeholder': 'Search'}))
