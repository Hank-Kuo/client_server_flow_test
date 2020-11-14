
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
#from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('', include('app.urls')), 
    path('', include('app_socket.urls')), 
]
