from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.conf import settings
import json
import time
from django.http import HttpResponse
from users.models import User,Token
from django.views.decorators.csrf import csrf_exempt

user_data={}
chart_data={ "score":{}, "translate_api":{} }

#------function------------
def get_user_data(username):
    # Type : String -> Json
    """Get user data 
    This function get the data which is score, endpoint, error, translate_api, rank
    from redis, the json is 
        user_data { "score": int, "endpoint" : string, "error" : string, 
        "translate_api" : string, "rank" : int }
    
    RETURN : user_data which is json format 

    """
    try:
        user_data["score"] = int(settings.CACHE1.zscore('score',username))
        user_data["endpoint"] = settings.CACHE1.lindex(username+"_user", 0) #endpoint
        user_data["error"] = settings.CACHE1.lindex(username+"_user", 1) # error
        user_data["translate_api"] = settings.CACHE1.lindex(username+"_user", 2) # error
        user_data["rank"] = 1
        print(user_data)
    except:
        pass
    return user_data 

def get_chart_data():
    """Get chart data 
    """
    try:
        for i in settings.CACHE1.zscan_iter("score"): 
            chart_data["score"][i[0]] = i[1]
    except:
        pass
    try:
        chart_data["translate_api"][i[0]] = settings.CACHE1.lindex(i[0]+"_user", 2)
    except:
        pass
    return chart_data

#-----------------------------------------

@accept_websocket
def ws_setting_token(request):
    """
    """
    while request.is_websocket():
        data = list(Token.objects.values())
        dit = {}
        for i in data:
            dit[i["token"]]=[i["is_valid"],i["username"]]
        try:
            message = request.websocket.wait(timeout=1)
            request.websocket.send(json.dumps(dit))
            print(dit)
        except Exception as e:
            pass

@accept_websocket
def ws_sand(request):
    """
    """
    while request.is_websocket():
        username = request.user.username
        user_data = get_user_data(username)
        try:
            message = request.websocket.wait(timeout=2)
            request.websocket.send(json.dumps(user_data))
            print(user_data)
        except Exception as e:
            pass
            

@accept_websocket
def ws_sand_chart(request):
    """
    """
    while request.is_websocket():
        chart_data = get_chart_data()
        try:
            message = request.websocket.wait(timeout=1.5)
            request.websocket.send(json.dumps(chart_data))
            print(chart_data)
        except Exception as e:
            pass
           


@csrf_exempt
def sandscore(request):
    username = request.user.username
    print(username)
    user_data = get_user_data(username)
    return HttpResponse(json.dumps(user_data))