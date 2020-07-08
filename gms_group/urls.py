"""gms_group URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('service/', Service.as_view(), name='service'),
    path('industries/', Industries.as_view(), name='industries'),
    path('about_us/', AboutUs.as_view(), name='about_us'),
    path('contact_us/', ContactUs.as_view(), name='contact_us'),
    path('thank_you/', ThankYou.as_view(), name='thank_you'),
]
