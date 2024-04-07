from django.shortcuts import render, redirect
from . import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from . import AutenticacaoForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario criado com sucesso')
            return redirect('helpdesk:index')

    return render(
        request, 'helpdesk/register.html', {'form': form, 'titulo':'Registrar novo usuario'}
    )

def login_view(request):

    form = AutenticacaoForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('helpdesk:index')
        messages.error(request, 'Login invalido')
                 

    return render(
        request, 'helpdesk/login.html', {'form': form, 'titulo':'Acessar sua conta'}
    )


def logout_view(request):
    auth.logout(request)
    return redirect('helpdesk:login')