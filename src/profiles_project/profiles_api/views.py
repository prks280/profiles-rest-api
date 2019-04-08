from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = ['cp','aliya','none','nana']
        return Response({'message':'hello', 'an_apiview':an_apiview})