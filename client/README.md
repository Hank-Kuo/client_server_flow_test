#!/bin/bash <br>
sudo su<br>
yum update -y<br>
yum install git -y<br>
cd home/ec2-user <br>
git clone https://gitlab.com/asdf024681029/sandbag.git<br>
yum install python35 -y<br>
yum install python35-pip -y<br>
/usr/bin/pip-3.5 install -r sandbag/sandbag/requirements.txt<br>
python3 sandbag/client/client_multi.py <br>