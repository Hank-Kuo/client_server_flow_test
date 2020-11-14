from flask import Flask,render_template
from flask import Response,request,jsonify
import json
import boto3


app = Flask(__name__)



name=""
dydb_header=""
dydb_value=""


# DB connect 
client = boto3.client('dynamodb',region_name="us-east-1")

@app.after_request
def apply_caching(response):
    global name
    global dydb_header
    response.headers["Name"] = name
    response.headers["Version"] = "v2"
    response.headers["From"] = "ECS"
    response.headers["DyDB_header"] = dydb_header
    return response
    

@app.route('/', methods=['GET', 'POST'])
def home():
    global name
    global last_time
    global dydb_header
    global dydb_value
    
    #get Name header 
    try :
        name = request.headers['Name']
    except : 
        name = "no Name"
    # get dydb_value_redis from redis 
    try:
        dydb_value = request.headers['dydb_value_redis']
    except : 
        dydb_value = "no Name"
    
    # get dynamodb value 
    try :
        response = client.get_item(
            TableName='sandbag',
            Key={
                'Id': {
                'S': '1',            
                }
            }
        )
        dydb_header =response["Item"]["dydb_header"]['S']
    except:
        dydb_header = "dydb get error"

    # put item to dynamodb 
    try:
        if(dydb_value!=dydb_header):
            response = client.put_item(
                TableName='sandbag',
                Item={
                    'Id': {
                        'S': '1',
                    },
                    'dydb_header':{
                        'S': str(dydb_value)
                    }
                }
            )
        else:
            print("no write")
    except :
        dydb_header = "dydb put error"

    
        
    return render_template('server_dydb.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
