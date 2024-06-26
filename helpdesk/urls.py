from django.urls import path
from helpdesk import views

app_name = 'helpdesk'

urlpatterns = [
    path('', views.index, name='index'),
    path('finalizado/', views.finalizado, name='finalizado'),
    path('search/', views.search, name='search'),

    #Chamado
    path('<int:call_id>/', views.call, name='call'),
    path('<int:call_id>/update/', views.update, name='update'),
    path('<int:call_id>/delete/', views.delete, name='delete'),
    path('<int:call_id>/finalizar/', views.finalizar, name='finalizar'),
    path('create/', views.create, name='create'),

    #user
    path('user/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_update/', views.user_update, name='user_update'),

]
