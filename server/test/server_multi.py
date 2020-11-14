from flask import Flask,render_template
from flask import Response,request
import json

app = Flask(__name__)

token=""

@app.after_request
def apply_caching(response):
    #print(response)
    global token
    response.headers["Token"] = token
    response.headers["Version"] = "v1"
    response.headers["From"] = "EC2"
    return response
    
@app.route('/', methods=['GET', 'POST'])
def home():
    global token
    try :
        print("test:")
        token =request.headers['Token']
        print(token)
    except:
        print("error")
    return render_template('server_V1_EC2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


