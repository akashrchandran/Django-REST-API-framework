import json

from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def read_database():
    with open('database.json', 'r') as f:
        return json.load(f)

@api_view(['GET', 'POST'])
def get_stocks(request):
    try:
        database = read_database()
        banana_type = database['bananaTypes']
        avail_stock = database['availableStock']
        response = {}
        for banana,stock in zip(banana_type,avail_stock):
            response[banana] = stock
        return Response({'error':False, 'bananaStock': response}, status=200)
    except Exception as e:
        return Response({'error':True, 'message': str(e)}, status=500)
    
def home(request):
    return HttpResponse("<h1>Welcome to Django REST API</h1><br><h4>Go to <a href='/rest/get_stocks'>/rest/get_stocks</a> to see the API</h4><br><h4>Go to my <a href='https://blog.akashrchandran.in/how-to-create-rest-api-using-django-rest-framework' target='_blank'>Blog</a> to see the detailed guide how I created this.</h4>")