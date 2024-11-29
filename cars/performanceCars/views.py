from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import PerformanceCars

# Create your views here.
def cars(request):
    template=loader.get_template('performanceCars.html')
    objects=PerformanceCars.objects.all().values()
    context={
        "performanceCars":objects,
    }
    return HttpResponse(template.render(context, request))