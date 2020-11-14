from flask import Flask,render_template
from flask import Response,request,jsonify
import json
import time
import mysql.connector 



app = Flask(__name__)


name=""
rds_header=""
last_time =0
rds_endpoint=""
rds_value=""
status=""




@app.after_request
def apply_caching(response):
    global name
    global rds_header
    global status
    global rds_value
    response.headers["Name"] = name
    response.headers["Version"] = "v2"
    response.headers["From"] = "EC2"
    response.headers["RDS_header"] = rds_header
    response.headers["rds_status"]=status
    response.headers["rds_value_redis"]=rds_value
    return response
    
flag=True

@app.route('/', methods=['GET', 'POST'])
def home():
    global name
    global last_time
    global rds_header
    global rds_endpoint
    global rds_value
    global status
    global flag
    

    
    #get Name header 
    try :
        name =request.headers['Name']
    except : 
        name = "no Name"
    # get rds info
    try:
        rds_endpoint=request.headers["rds_endpoint"]
        rds_value=request.headers["rds_value"]
    except:
        print("no rds endpoint and rds value")
    
    if(flag==True):
        # connect mysql and get mysql data
        try :
            mydb = mysql.connector.connect(
                host=rds_endpoint,      
                user="admin",    
                passwd="123456789",   
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE sandbag_db")
            status="table success"
        except:
            status="table fail"
            print("error create table ")
        # create site 
        try:
            mydb = mysql.connector.connect(
                    host=rds_endpoint,      
                    user="admin",    
                    passwd="123456789",   
                    database="sandbag_db"
                )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),header VARCHAR(255))")
            status="success"
        except :
            status="site fail"
            print("error create site ")

        # insert value 
        try :
            mydb = mysql.connector.connect(
                host=rds_endpoint,      
                user="admin",    
                passwd="123456789",   
                database="sandbag_db"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO sites (name,header) VALUES (%s,%s)"
            val = ("sandbag","ecloudvalley")
            mycursor.execute(sql, val)
            mydb.commit()    
            status="success"
            flag=False
        except :
            status="value fail"
            print("error insert")

     # get rds header 
    try :
        mydb = mysql.connector.connect(
            host=rds_endpoint ,     
            user="admin",    
            passwd="123456789",   
            database="sandbag_db"
        )
        mycursor = mydb.cursor()
        sql = "SELECT header FROM sites WHERE name ='sandbag'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        rds_header = myresult[0]
    except:
        rds_header = "rds get error"
    
    
    # update 
    if(rds_header !=rds_value):
        # if different -> update 
        try :
            mydb = mysql.connector.connect(
                host=rds_endpoint,      
                user="admin",    
                passwd="123456789",   
                database="sandbag_db"
            )
            mycursor = mydb.cursor()
            sql = "UPDATE sites SET header = "+ "'" + rds_value+ "'" +"WHERE name = 'sandbag'"
            mycursor.execute(sql)
            mydb.commit()   
            status="success"
            rds_header=rds_value
        except :
            status="update fail"
            print(status)
    else:
        print("no update")
    
    print("rds_header is ",rds_header)
    return render_template('server_rds.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
