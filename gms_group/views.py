from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='index.html'

class Service(TemplateView):
    template_name='service.html'

class Industries(TemplateView):
    template_name='industries.html'

class AboutUs(TemplateView):
    template_name='about_us.html'

class ContactUs(TemplateView):
    template_name='contact_us.html'

class ThankYou(TemplateView):
    template_name='thank_you.html'
