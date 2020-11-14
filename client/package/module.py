import time
import requests


"""Check Header score and condition
Attribute :
    judge_score : token -> 100, version -> 50, from_type -> 50
    judge : 0 -> token, 1 -> version, 2 -> from_type 
"""
judge_score = [100,20,20]

judge = { 0: { "correct" : judge_score[0] ,"wrong" : 0-judge_score[0]} , 
        1 : { "v1" : judge_score[1] ,"v2" : 0-judge_score[1], "" : 0-judge_score[1] } , 
        2 : { "EC2" : judge_score[2], "ECS" : 0-judge_score[2] , "" : 0-judge_score[2]  } }


def transfer(t):
    # Type : str -> int 
    """Transfer time type
    Let the string time which like "2019-8-8 6:30" transfer to integer time which is 
    second based. 
    
    Args :
        t : The time which want to transfer to integer time.  
    """
    transfer_time = time.strptime(t, "%Y-%m-%d %H:%M")
    return int(time.mktime(transfer_time))
        
def transfer_endpoint(endpoint):
    # Type : str -> str 
    """Transfer endpoint 
    It will check the endpoint start with "http", if it doesn't start with http, wll add
    the "http://" in front  the endpoint. 
    
    Args : 
        endpoint : which want to transfer to endpoint with the "http://" .
    
    Return :
        endpoiont : Already transfered endpoint. 
    """
    if(endpoint.startswith("http")):
        return endpoint
    else:
        endpoint = "http://"+endpoint
        return endpoint

def get_header(user_response,endpoint,token):
    # Type : list, str, str -> list 
    """Get header 


    """
    try:
        response=requests.get(endpoint,headers={'Token':token},timeout=3) # sending requests
        user_response["token"]=response.headers['Token']
        user_response["version"]=response.headers['Version']
        user_response["from_type"]=response.headers['From']
    except:
        print("no header")
    return user_response

def get_user(r1):
    # Type : redis -> list 
    """Transfer time type

    """
    user=[]
    for key in r1.scan_iter():
        if( "user" in key):
            username = key.replace("_user", "")
            user.append(username)
    return user

def check_header(id,ans,response,setting_time):
    # Type : int, str, str, int -> int
    """Check the request's header 
    Check the request header is correct or not, using 
    Args :
        id : 
        ans : 
        response :
        setting_time :
    """
    if(id==0):
        if(ans == response):
            response = "correct"
            return judge[id][response]
        else:
            response = "wrong"
            return judge[id][response]
    else :
        if(time.time() < setting_time):
            return judge[id][response]
        else:
            if(response==""):
                return judge[id][response]
            else:
                return 0-judge[id][response]

class User:
    def __init__(self, username, endpoint):
        # Type : str, str -> None
        """
        """
        self.username = username
        self.endpoint = endpoint
        self.score = 0
        self.error_ms = ""
    
    def setUsername(self,user,index):
        # Type : list, int -> None
        """
        """
        username = user[index]
        self.username = username
            
    def setEndpoint(self,r1):
        # Type : redis -> None
        try:
            endpoint = r1.lindex(self.username+"_user",0) 
            endpoint = transfer_endpoint(endpoint)
            self.endpoint = endpoint
        except:
            print("redis error endpoint ")
    def setError(self,user_response,r):
        # Type : list, redis -> None
        error_ms = ("token : "+ user_response["token"]+"\n"
                + "version : "+user_response["version"]+"\n"+ 
                "Type : " +user_response["from_type"])
        self.error_ms = error_ms
        try:
            r.lset(self.username+'_user', 1,error_ms) 
        except:
            print("redis error errormessage ")

    def setScore(self,r):
        # redis -> None 
        """
        save the score to the Class and 
        """
        try:
            r.zincrby(name="score",value=self.username,amount=self.score)
        except:
            print("redis error score")


