from django.shortcuts import render, redirect
from . import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from . import AutenticacaoForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='helpdesk:login')
def logout_view(request):
    auth.logout(request)
    return redirect('helpdesk:login')

@login_required(login_url='helpdesk:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)


    if request.method != 'POST':
        return render(
            request, 'helpdesk/register.html', {'form': form, 'titulo':'Atualizar usuario'}
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request, 'helpdesk/register.html', {'form': form, 'titulo':'Atualizar usuario'}
        )
    
    form.save()
    return redirect('helpdesk:user_update')

    

    
