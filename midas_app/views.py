from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PersonaForm
from .models import Persona, PersonXML
import dicttoxml


def index(request):
    return render(request, 'base.html')


def persona_new(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('nombre'))
            p1 = form.save()
            print(type(p1))
            x1 = PersonXML(form.cleaned_data.get('nombre'), form.cleaned_data.get('apellido'))
            # p1 = PersonXML(form.cleaned_data.get('nombre'), form.cleaned_data.get('apellido'))

            xml = dicttoxml.dicttoxml(x1.__dict__,attr_type=False, custom_root='Person')
            print(xml)

        return redirect('bienvenida')
    else:
        form = PersonaForm()

    return render(request, 'persona_edit.html', {'form': form})
