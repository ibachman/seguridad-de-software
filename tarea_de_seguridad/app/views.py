from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect

from .forms import *
# Create your views here.
def register(request):
    form=registroForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/../')
    return render_to_response("registro.html",locals(), context_instance=RequestContext(request))

def home(request):
    return render_to_response("home.html",locals(), context_instance=RequestContext(request))
def login(request):
    return render_to_response("login.html",locals(), context_instance=RequestContext(request))
