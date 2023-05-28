import json

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