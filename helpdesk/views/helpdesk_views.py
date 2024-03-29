from django.shortcuts import render, get_object_or_404
from helpdesk.models import Call

# Create your views here.
def index(request):
    calls = Call.objects.filter(show=True).order_by('-id')
    context = {
        'calls':calls,
    }
    return render(request, 'helpdesk/index.html', context)

def call(request, call_id):
    chamado = get_object_or_404(Call, pk=call_id, show=True)

    context = {
        'calls':chamado,
    }
    return render(request, 'helpdesk/call.html', context)
