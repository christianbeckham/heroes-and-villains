from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

# Create your views here.


@api_view(['GET'])
def supers_list(request):
    queryset = Super.objects.all()
    serializer = SuperSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data, status=status.HTTP_200_OK)
