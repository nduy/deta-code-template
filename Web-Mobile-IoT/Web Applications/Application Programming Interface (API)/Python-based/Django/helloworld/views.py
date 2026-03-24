#from django.shortcuts import render
# Create your views here.
import json
from django.http import HttpResponse

def index(request):
    param =999;
    param = (request.GET.get("param"))
    item = {"message": "Hello World!", "param": param}
    
    return HttpResponse(json.dumps(item));