from django.urls import path
from helpdesk import views

app_name = 'helpdesk'

urlpatterns = [
    path('', views.index, name='index'),
]
