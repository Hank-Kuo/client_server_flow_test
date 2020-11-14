import threading 
import redis
import uuid
from package.module import *

# connect redis
r = redis.Redis(host='hank-001.bwwxt6.0001.use1.cache.amazonaws.com', port=6379, charset="utf-8",decode_responses=True)
r1 = redis.Redis(host='hank-003.bwwxt6.0001.use1.cache.amazonaws.com', port=6379, charset="utf-8",decode_responses=True) 

# initial variable -- setting time for version and from_type
version_time = transfer("2019-8-8 6:30")
from_type_time = transfer("2019-8-8 6:30")


def stresser(): 
    global all_user 
    index = 0 # 
    last_time = 0 
    while True : 
        # create token
        TOKEN = str(uuid.uuid4()) 
        SCORE = 0

        user_response = { "token" : "","version" : "","from_type" : "" }

        if (time.time() - last_time) > 5:
            last_time = time.time()
            all_user = get_user(r1)

        # create User
        if(len(all_user)>0):
            user = User(username="", endpoint="")
            user.setUsername(all_user, index)
            user.setEndpoint(r1)   
            
            # get header 
            user_response = get_header(user_response,user.endpoint,TOKEN)
            
            # check header
            SCORE += check_header(0,TOKEN,user_response["token"],0)
            SCORE += check_header(1,None,user_response["version"],version_time)
            SCORE += check_header(2,None,user_response["from_type"],from_type_time)
            user.score = SCORE
            user.setError(user_response,r)
            user.setScore(r)
            
            print(user.username)
            print(user.endpoint)
            print(user_response)
            print(user.error_ms)
            print(user.score)
            print("------------------------------------------------")
        else:
            print("no user in Redis")
 
        # loop user
        index+=1
        if(index>=len(all_user)):
            index=0


def _threads_(): 
    c= threading.Thread(target=stresser) 
    d= threading.Thread(target=stresser)
    a= threading.Thread(target=stresser)
    e= threading.Thread(target=stresser)
    z= threading.Thread(target=stresser)
    c.start()
    c.join()
    d.start()
    d.join()
    a.start()
    a.join()
    e.start()
    e.join()
    z.start()
    z.join()

def main():
	time.sleep(1)
	_threads_() 

main()
