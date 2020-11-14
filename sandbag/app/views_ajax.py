from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from users.models import Token
from uuid import uuid4
import requests
from django.conf import settings

#------function---------------

def set_endpoint(username,endpoint):
    settings.CACHE.lset(username+'_user', 0,endpoint) 
    print("save endpoint")

def set_translate_api(username,ans):
    settings.CACHE.lset(username+'_user', 2,ans) 
    print("save...")

#----------------------------

@csrf_exempt
def sandept(request):
    # Type : request -> Json 
    """
    
    """
    endpoint = request.POST.get('endpoint', None)
    context = {"result":endpoint}
    username = request.user.username
    set_endpoint(username,endpoint[1:-1])
    return HttpResponse(json.dumps(context))

@csrf_exempt
def crt_token(request):
    token = int(request.POST.get('token', None))
    context = {"result":token}
    for i in range(token):
        rand_token = uuid4()
        db = Token(token=rand_token, username='')
        db.save()
    return HttpResponse(json.dumps(context))

@csrf_exempt
def translept(request):
    endpoint = request.POST.get('endpoint', None)
    endpoint = endpoint[1:-1]
    username = request.user.username
    print(endpoint)
    # endpoint = "https://h1e54y0sel.execute-api.us-east-1.amazonaws.com/dev/translate-text"
    payload = {'API_Endpoint': endpoint}
    result="Your API is timeout. Pleas try again"
    try:
        req = requests.request('POST', 'https://h1e54y0sel.execute-api.us-east-1.amazonaws.com/dev/translate-api',json=payload,timeout=15)
        result = req.json()["body"]
    except:
        pass
    if(result=="Your API is working perfectly."):
        set_translate_api(username,"true")
    else:
        set_translate_api(username,"false")
    context = {"result":result}
    return HttpResponse(json.dumps(context))