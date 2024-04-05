from django.shortcuts import render, get_object_or_404, redirect
from helpdesk.models import Call
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    calls = Call.objects.filter(show=True).order_by('-id')

    paginator = Paginator(calls, 3)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'titulo': 'Consulta de chamado'
    }
    return render(request, 'helpdesk/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('helpdesk:index')

    calls = Call.objects.filter(show=True).filter(title__contains=search_value).order_by('-id')

    paginator = Paginator(calls, 3)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'titulo': 'Consulta de chamado',
        'calls':page_obj,
        'search_value': search_value,
        'page_obj': page_obj,
    }
    return render(request, 'helpdesk/index.html', context)

def call(request, call_id):
    chamado = get_object_or_404(Call, pk=call_id, show=True)

    context = {
        'titulo': 'Consulta de chamado',
        'calls':chamado,
    }
    return render(request, 'helpdesk/call.html', context)
