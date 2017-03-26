from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def func(req, url):
    resp = requests.get(url)
    return HttpResponse(resp)