from django.shortcuts import render, get_object_or_404, redirect
from helpdesk.models import Call
from django import forms
from django.urls import reverse

class CallForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['description'].widget.attrs.update({
            'class':'form-control'
        })

    class Meta:
        model = Call
        fields = 'title', 'category', 'description',
        


# Create your views here.
def create(request):

    form_action = reverse('helpdesk:create')

    

    if request.method == 'POST':
        form = CallForm(request.POST)
        context = {
            'titulo': 'Novo Chamado',
            'form': form,
            'form_action':form_action
        }

        if form.is_valid():
            call = form.save()
            return redirect('helpdesk:update', call_id=call.id)
            

        return render(request, 'helpdesk/create.html', context)

    context = {
            'titulo': 'Novo Chamado',
            'form': CallForm(),
            'form_action':form_action,
        }

    return render(request, 'helpdesk/create.html', context)

def update(request, call_id):

    call = get_object_or_404(Call, pk=call_id, show=True)

    form_action = reverse('helpdesk:update', args=(call_id,))

    

    if request.method == 'POST':
        form = CallForm(request.POST, instance=call)
        context = {
            'titulo': 'Editar Chamado',
            'form': form,
            'form_action':form_action,
        }

        if form.is_valid():
            call = form.save()
            return redirect('helpdesk:update', call_id=call.id)
            

        return render(request, 'helpdesk/create.html', context)

    context = {
            'titulo': 'Novo Chamado',
            'form': CallForm( instance=call),
            'form_action':form_action,
        }

    return render(request, 'helpdesk/index.html', context)
