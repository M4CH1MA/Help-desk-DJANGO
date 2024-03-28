from django.shortcuts import render
from helpdesk.models import Call

# Create your views here.
def index(request):
    calls = Call.objects.filter(show=True).order_by('-id')
    context = {
        'calls':calls,
    }
    return render(request, 'helpdesk/index.html', context)

def call(request, call_id):
    chamado = Call.objects.get(id=call_id)
    context = {
        'calls':chamado,
    }
    return render(request, 'helpdesk/call.html', context)
