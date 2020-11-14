from django.urls import path
from . import views

urlpatterns = [
    path('ws_sand/', views.ws_sand),
    path('ws_sand_chart/', views.ws_sand_chart),
    path('ws_setting_token/', views.ws_setting_token),
    path('sandscore/',views.sandscore),
   
]