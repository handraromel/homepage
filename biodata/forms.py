from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=25)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=25)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(),
        help_text="Your message"
    )
