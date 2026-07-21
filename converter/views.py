from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
import os
import tempfile

def index(request):
    return render(request, 'converter/index.html')

def health(request):
    return JsonResponse({'status': 'ok', 'app': 'AudioPro'})
