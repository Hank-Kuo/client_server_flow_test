# Flow Test
## Client 
### Introduce
The Hacker will use HTTP flood request to attack Client server.
## Server
### Introduce
The Client need to maintance their architecture to avoid the http flood request attck, so client need to build flexilbe architecture to face this attack. 
## Sangabag
### Introduce 
It's Dashboard that clients can see their score

### Tool
- It's all by Python, the framework is Django, and use redis to record the real time score. In dashboard, use the socket to send score.
