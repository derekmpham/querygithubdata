# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
	return HttpResponse('Hello World!')

def test(request):
	return HttpResponse('My second view!')

def profile(request):
	req = requests.get('https://api.github.com/users/derekmpham')
	content = req.text
	return HttpResponse(content)
