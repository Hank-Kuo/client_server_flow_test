# Flow Test
## Introduce 
This project is mainly used to conduct traffic test for users. By transmitting a large amount of traffic, users can accept a large number of requests, and will add points and deduct points according to the answers to the reply. And here you will need to use the AWS cloud platform for testing. The user builds a website through EC2 on AWS, maintains a website, and scales according to the size of the traffic.

## Overview 
- Client website
- Server website
- Dashboard website

## Architecture
- In Client Side 

![](https://i.imgur.com/j3eZiLy.png)

- In Server Side 

![](https://i.imgur.com/FivNHL0.png)

## Technical Document 
### Prequestion:
- Framework: Flask, Django
- DB: Redis
- Judge the Response in Header:
    - Is token correct
    - Is version correct
    - Is from_type correct
### Client

#### Introduce
send request to user side, and calculate the score, then save to redis.

#### Detail
- Python environment: python2
- Setup:
```
#!/bin/bash
sudo su
yum update -y
yum install git -y
cd home/ec2-user
git clone https://gitlab.com/asdf024681029/sandbag.git
yum install python35 -y
yum install python35-pip -y
/usr/bin/pip-3.5 install -r sandbag/sandbag/requirements.txt
python3 sandbag/client/client_multi.py
```
- redis host is in client_multi.py
- Score calculate
    - token: 100
    - version: 50
    - from_type: 50
- client_multi.py
- module.py
    - **transfer function**: transfer time type
    - **transfer_endpoint function**: check the endpoint start with "http", if it doesn't start with http, wll add http:// to origin string
    - **get_header function**: Get header values from response
    - **get_user function**: Get all user from redis
    - **check_header function**: Check the request header is correct or not
    - **User class**: Setting user the basic information, like username, endpoint, score, error_message
### Server
#### Introduce 
User need use this file (server_v2_ECS.py) to host website in AWS environment, and accept lost of requests .
#### Detail
- Python environment: python2
- Setup
```
#!/bin/bash
sudo yum update -y
sudo yum install git -y 
sudo pip install flask
cd home/ec2-user 
sudo git clone https://gitlab.com/asdf024681029/sandbag.git 
sudo python sandbag/server/server_v2_ECS.py
```
- server_v2_ECS.py
    - use server_V2_ECS.html which is in template folder to render page 
    - when requests comes, server will add 'Token', 'Version' and 'From' to header, then response to sender
    - port is in 80
### Sandbag
#### Introduce
This is dashboard, users can through this to see their score, then check error message.
#### Detail 
- Python environment: python3, Django==2.1.*
- Setup
```
#!/bin/bash
sudo su
yum update -y && yum install git -y
cd home/ec2-user
git clone https://gitlab.com/asdf024681029/sandbag.git
yum install python35 -y
yum install python35 -y && yum install python35-pip -y
/usr/bin/pip-3.5 install -r sandbag/sandbag/requirements.txt
cd sandbag/dwbsocket/
python3 setup.py install
cd ..
python3 sandbag/manage.py makemigrations
python3 sandbag/manage.py migrate
python3 sandbag/manage.py runserver 0.0.0.0:80
```
- Database: Sqlite3 
    - record user information
- Architecture
    - traditional MVVM
    - templates
        - All Html file in here
    - static
        - All CSS or JS in here
    - users
        - About login page, logout and register page
    - app
        - About index page, chart page, setting page, setting-token page
        - Two role: admin, stuff
            - admin: can get in all page
            - stuff: only can get in index, chart page
    - app_socket
        - Handle the socket API, it uses in chart page, setting-token page, 
    - sandbag
        - It's main program, all settign in here.
        - setting redis url in here

### dwbsocket
#### Introduce 
This is a kind of the socket library in python.
