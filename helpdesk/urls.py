from django.urls import path
from helpdesk import views

app_name = 'helpdesk'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    path('<int:call_id>/', views.call, name='call'),
    path('create/', views.create, name='create'),

]
