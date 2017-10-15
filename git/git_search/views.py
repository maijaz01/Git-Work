from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import urllib
import json


def indexPage(request):
    api = 'https://api.github.com/search/users?q=%s' % 'maijaz01'
    api_data = urllib.urlopen(api)
    api_data = json.loads(api_data.read())
    return render_to_response('index.html', {'data': api_data['items']})