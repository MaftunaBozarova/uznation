from django import forms
from .models import Feedback
from ckeditor.widgets import CKEditorWidget


class FeedBackForm(forms.ModelForm):
    comment = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'comment')
