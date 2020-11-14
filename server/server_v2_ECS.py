from flask import Flask,render_template
from flask import Response,request
import json

app = Flask(__name__)


name=""
count=0
@app.after_request
def apply_caching(response):
    #print(response)                                                                                                                  
    global name
    global count
    response.headers["Token"] = name
    response.headers["Version"] = "v2"
    response.headers["From"] = "ECS"
    count+=1
    print(count)
    for i in range(10):
        for j in range(10):
            print(i*j)
    return response

    
@app.route('/', methods=['GET', 'POST'])
def home():
    global name
    try :
        print("test:")
        name =request.headers['Token']
        print(name)
    except:
        print("error")
    return render_template('server_V2_ECS.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



