from django import forms
from django.core.mail import send_mail
from django.template.loader import get_template

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField()
    inquiry = forms.CharField(required=True)

    def send_email(self):
        template = get_template('contact_form.txt')
        content = {
            'name' : self.cleaned_data['name'],
            'email' : self.cleaned_data['email'],
            'phone' : self.cleaned_data['phone'],
            'inquiry' : self.cleaned_data['inquiry'],
        }
        content = template.render(content)
        email = self.cleaned_data['email']
        send_mail(
            "New Q&A form email",
            content,
            "K-Gen Group",
            ['info@kgen.group'],
            fail_silently=False,
        )
