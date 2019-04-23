# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/catalog.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
