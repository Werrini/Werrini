from django import forms
from ckeditor.fields import RichTextField

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message here'}), required=True)
    test = RichTextField()