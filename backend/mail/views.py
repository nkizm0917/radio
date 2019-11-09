from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Mail


def index(request):
    template = loader.get_template('mail/index.html')
    return render(request, 'mail/index.html')

def results(request, mail_id):
    mail = get_object_or_404(Mail, pk=mail_id)
    return render(request, 'mail/results.html', {'mail': mail})
