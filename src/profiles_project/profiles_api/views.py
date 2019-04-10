from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets


class HelloAPIView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = ['cp','aliya','none','nana']
        return Response({'message':'hello', 'an_apiview':an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message = 'hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self,request, pk=None):
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        return Response({'method':'delete'})

class Hello_Viewset(viewsets.ViewSet):

    def list(self, request):
        an_viewset = ['new','cp', 'aliya', 'none', 'nana']
        return Response({"message":an_viewset})

