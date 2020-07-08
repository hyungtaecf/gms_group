from django.views.generic import TemplateView, FormView
from .forms import ContactForm

class Home(TemplateView):
    template_name='index.html'

class Service(TemplateView):
    template_name='service.html'

class Industries(TemplateView):
    template_name='industries.html'

class AboutUs(TemplateView):
    template_name='about_us.html'

class ContactUs(FormView):
    form_class = ContactForm
    template_name='contact_us.html'
    success_url = '/thank_you/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class ThankYou(TemplateView):
    template_name='thank_you.html'
