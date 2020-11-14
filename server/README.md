

#!/bin/bash <br>
sudo yum update -y <br>
sudo yum install git -y <br>
sudo pip install flask <br>
cd home/ec2-user  <br>
sudo git clone https://gitlab.com/asdf024681029/sandbag.git <br>
sudo python sandbag/server/server_v2_ECS.py<br>








