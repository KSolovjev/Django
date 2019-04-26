# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

links_menu = [{'href': 'products_all', 'name': 'all'},
{'href': 'products_home', 'name': 'home'},
{'href': 'products_office', 'name': 'office'},
{'href': 'products_modern', 'name': 'modern'},
{'href': 'products_classic', 'name': 'classic'}]

context = {'name': 'ivan', 'array': [1, 2, 3, 4, 5]}

def main(request):
    return render(request, 'mainapp/index.html', context)

def products(request):
    return render(request, 'mainapp/products.html', links_menu)

def contacts(request):
    return render(request, 'mainapp/contacts.html', context)
