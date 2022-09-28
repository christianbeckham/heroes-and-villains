from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer

# Create your views here.


@api_view(['GET'])
def super_types_list(request):
    if request.method == 'GET':
        types = SuperType.objects.all()
        serializer = SuperTypeSerializer(types, many=True)
        return Response(serializer.data)
