from flask import Flask,render_template
from flask import Response,request
import json

app = Flask(__name__)


name=""

@app.after_request
def apply_caching(response):
    #print(response)
    global name
    response.headers["Name"] = name
    response.headers["Version"] = "v2"
    response.headers["From"] = "EC2"
    return response
    
@app.route('/', methods=['GET', 'POST'])
def home():
    global name
    try :
        print("test:")
        name =request.headers['Name']
        print(name)
    except:
        print("error")
    return render_template('server_V2_EC2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


