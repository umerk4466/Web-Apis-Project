from django.urls import re_path,path,include
from . import views


urlpatterns = [
     path('', views.hello, name="hello"),
     # django rest_api requests:
     # re_path(r'^api/user/update/(?P<username>\w+)/(?P<password>.+)/(?P<reg_no>.+)/(?P<fname>.+)/(?P<email>.+)/$', views.update_user_data, name="update_user_data"),
     
     # user api urls
     path('api/get/user/', views.get_user_data, name="get_user_data"),
     path('api/register/user/', views.set_user_data, name="set_user_data"),
     path('api/update/user/', views.update_user_data, name="update_user_data"),
     # vehicle api urls
     path('api/get/user/vehicle/', views.get_user_vehicle, name="get_user_vehicle"),
     path('api/get/vehicle/', views.get_vehicle, name="get_vehicle"),
     path('api/add/vehicle/', views.add_vehicle, name="add_vehicle"),
     path('api/remove/vehicle/', views.remove_vehicle, name="remove_vehicle"),
     # reminder api urls
     path('api/get/user/reminder/', views.get_user_reminder, name="get_user_reminder"),
     path('api/get/reminder/', views.get_reminder, name="get_reminder"),
     path('api/add/reminder/', views.add_reminder, name="add_reminder"),
     path('api/remove/reminder/', views.remove_reminder, name="remove_reminder"),
     path('api/update/reminder/', views.update_reminder, name="update_reminder"),



     
     
     



]
