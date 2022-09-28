from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        types = SuperType.objects.all()
        serializer = SuperTypeSerializer(types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def super_types_detail(request, pk):
    type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(type)
        return Response(serializer.data, status=status.HTTP_200_OK)
