from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from super_types.models import SuperType

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        queryset = Super.objects.all()
        param = request.query_params.get('type')
        if param:
            query = queryset.filter(super_type__type=param)
            serializer = SuperSerializer(query, many=True)
            custom_response = serializer.data
        else:
            super_types = SuperType.objects.all()
            custom_response = {'heroes': [], 'villains': []}
            for super_type in super_types:
                query = queryset.filter(super_type__id=super_type.id)
                serializer = SuperSerializer(query, many=True)
                if super_type.id == 1:
                    custom_response['heroes'] = serializer.data
                elif super_type.id == 2:
                    custom_response['villains'] = serializer.data
        return Response(custom_response, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
