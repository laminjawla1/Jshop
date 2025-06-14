from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from . import service

@csrf_exempt
def products(request):
    """products method to support both GET and POST request"""

    # Retrieve all products
    if request.method == "GET":
        return JsonResponse(service.get_products(), safe=False)

    # Add a new product
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            return JsonResponse(service.add_product(data).serialize(), status=201, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400, safe=False)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)


def get_product(request, product_id):
    if request.method == "GET":
        try:
            return JsonResponse(service.get_product(product_id), safe=False) 
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=404)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)
