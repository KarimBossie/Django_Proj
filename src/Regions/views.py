from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def DjanGoBookStoRe_view(request):
    out = '<ul>'
    regions = models.Region.objects.all()
    for reg in regions:
        out += f"<li>Region { reg.name } </li>"
    out += '</ul>'
    return HttpResponse(out)
