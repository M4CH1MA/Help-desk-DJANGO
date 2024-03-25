from django.shortcuts import render
from helpdesk.models import Call

# Create your views here.
def index(request):
    calls = Call.objects.all()
    context = {
        'calls':calls,
    }
    return render(request, 'helpdesk/index.html', context)
