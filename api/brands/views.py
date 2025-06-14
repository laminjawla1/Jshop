from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from brands.serializers import BrandSerializer

from . import service


@csrf_exempt
@api_view(["GET", "POST"])
def brands(request):
    method = request.method

    if method == "POST":
        serialized_data = BrandSerializer(data=request.data)
        if serialized_data.is_valid():
            return service.add_brand(serialized_data)
        return Response(serialized_data.errors, status=400)

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def brand(request, brand_id):
    method = request.method
    methods = {
        "GET": Response(service.get_brand(brand_id))
    }

    try:
        return methods.get(method)
    except Exception as e:
        return Response({"message": str(e)}, status=404)