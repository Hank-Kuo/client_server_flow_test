from django.urls import path
from . import views, views_ajax

urlpatterns = [
    path('index/', views.index, name='index'),
    path('chart/', views.chart, name='chart'),
    path('setting/', views.setting, name='setting'),
    path('token/',views.token,name="token"),
    path('ajax_sandept',views_ajax.sandept,name='ajax_sandept'),
    path('ajax_token',views_ajax.crt_token,name='ajax_token'),
    path('ajax_translept',views_ajax.translept,name='ajax_translept'),
]
