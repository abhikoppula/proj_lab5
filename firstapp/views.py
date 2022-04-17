from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def firstView(request):
    return JsonResponse({"Name": "Hello World!"})