# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import login
from django.conf import settings

from models import *
from apps.login.forms import DocumentForm,RegisterForm
from django.contrib.redirects.models import Redirect
from psycopg2.psycopg1 import cursor
from django.db import connection

def list(request):
    # Handle file upload
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document1(docfile = request.FILES['docfile'])
            newdoc.owner=request.user
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('list')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document1.objects.filter(owner=request.user)

    # Render list page with the documents and the form
    return render_to_response(
        'login/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def register(request):
    
    
    form= RegisterForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            user= form.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
            return redirect('list')
    
    ctx = {'form':form }
         
    return render_to_response('login/register.html', ctx, context_instance = RequestContext(request))
