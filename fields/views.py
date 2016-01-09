#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fields.models import App
from fields.serializers import AppSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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

@csrf_exempt
def app_list(request):
    """
    List all code apps, or create a new app.
    """
    if request.method == 'GET':
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
