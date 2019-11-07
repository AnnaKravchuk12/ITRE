from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime

def main(request):
    return render(request, 'main.html', {'parameter': "Привіт від Ані"})


def health(request):
    response = {
            'date': datetime.now().strftime("%Y-m-%d %H:%M:%S"), 
            'current_page': request.path,
            'server_info': os.uname(),
            'client_info': request.META['HTTP_USER_AGENT']
    }
    return JsonResponse(response)

