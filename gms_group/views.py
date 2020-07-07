from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='index.html'

class Service(TemplateView):
    template_name='service.html'
