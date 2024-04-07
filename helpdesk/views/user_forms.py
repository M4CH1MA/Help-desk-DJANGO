from django.shortcuts import render, redirect
from . import RegisterForm
from django.contrib import messages

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