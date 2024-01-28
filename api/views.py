from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializer import TodoSerializer
from .models import Todo
from  django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    
    if request.method =='GET':
        json_data = request.body
        print(json_data)
        stream =  io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream=stream)
        print(python_data)
        id =  python_data.get('id', None)
        print(id)
        try:
            data = Todo.objects.get(id=id)
            serializer =  TodoSerializer(data)
            print(serializer.data)
            return JsonResponse(serializer.data)
        except:
            data = {'error':'No recode Found'}
            return JsonResponse(data)

    if request.method =="POST":
        try:
            json_data =  request.body
            stream  = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream= stream)
            serializer =  TodoSerializer(data =  python_data)
            if serializer.is_valid():
                res = {'mes':'Created'}
                serializer.save()
                return JsonResponse(res)
        except:
            data = {'error':'No recode Found'}
            return JsonResponse(data)

    if request.method == "PUT":
        try:
            json_data =  request.body
            stream  = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream= stream)
            id =  python_data.get('id')
            qureyData =  Todo.objects.get(id = id) 
            serializer =  TodoSerializer(qureyData, data =  python_data, partial= True)
            if serializer.is_valid():
                res = {'mes':'Updated'}
                serializer.save()
                return JsonResponse(res)
        except:
            data = {'error':'No recode Found'}
            return JsonResponse(data)

    if request.method == "DELETE":
        try:
            json_data =  request.body
            stream  = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream= stream)
            id =  python_data.get('id')
            qureyData =  Todo.objects.get(id = id) 
            qureyData.delete()
            res =  {'mes':'Deleted'}
            return JsonResponse(res)
        except:
            data = {'error':'No recode Found'}
            return JsonResponse(data)