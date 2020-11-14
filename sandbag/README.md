# sandbag
1. user data 

#!/bin/bash<br>
sudo su<br>
yum update -y && yum install git -y<br>
cd home/ec2-user<br>
git clone https://gitlab.com/asdf024681029/sandbag.git<br>
yum install python35 -y<br>
yum install python35 -y && yum install python35-pip -y<br>
/usr/bin/pip-3.5 install -r sandbag/sandbag/requirements.txt <br>
cd sandbag/dwbsocket/<br>
python3 setup.py install<br>
cd ..<br>
python3 sandbag/manage.py makemigrations<br>
python3 sandbag/manage.py migrate<br>
python3 sandbag/manage.py runserver 0.0.0.0:80<br>

2. 
/usr/bin/pip-3.5 install Django==2.1.*<br>
/usr/bin/pip-3.5 install redis<br>
/usr/bin/pip-3.5 install requests<br>
/usr/bin/pip-3.5 install -r requirements.txt<br>
