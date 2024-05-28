from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection
from sqlparse import format

def home(request):
    qs = Product.objects.all()
    serialized_data = serialize('json', qs)

    q = list(connection.queries)
    for qs in q:
        sqlformatted = format(str(qs["sql"]), reindent = True)  
        print(sqlformatted)
    serialized_data = json.loads(serialized_data)

    return JsonResponse(serialized_data, safe = False, status=200)



