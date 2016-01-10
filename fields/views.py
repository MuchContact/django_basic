#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fields.models import App
from fields.serializers import AppSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class AppList(APIView):
    """
    List all code apps, or create a new app.
    """
    def get(self, request, format=None):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return JSONResponse(serializer.data)

    def post(self, request, format=None):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

class AppDetail(APIView):
    """
    Retrieve, update or delete a app instance.
    """
    def get_object(self, pk):
        try:
            return App.objects.get(pk=pk)
        except App.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = AppSerializer(app)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        app = self.get_object(pk)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
