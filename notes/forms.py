from django import forms
from .models import Notes



class NotesForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    notes = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Note Description","rows":20, "cols":150}))

    class Meta:
        model = Notes
        fields = ['title','notes']

    