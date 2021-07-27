from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'home'

urlpatterns = [
    #path('', views.MainView.as_view(), name='all'),
    path('', TemplateView.as_view(template_name='home/main.html')),
]