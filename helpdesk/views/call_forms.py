from django.shortcuts import render, get_object_or_404, redirect
from helpdesk.models import Call
from django.core.paginator import Paginator
from django import forms

class CallForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['description'].widget.attrs.update({
            'class':'form-control'
        })

    class Meta:
        model = Call
        fields = 'title', 'description',
        


# Create your views here.
def create(request):

    if request.method == 'POST':
        context = {
            'titulo': 'Novo Chamado',
            'form': CallForm(request.POST),
        }

        return render(request, 'helpdesk/create.html', context)

    context = {
        'titulo': 'Novo Chamado',
        'form': CallForm(),
    }

    return render(request, 'helpdesk/create.html', context)