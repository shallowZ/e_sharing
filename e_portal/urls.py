from django.urls import path,include
from .views import log, customer, manager, operator
from django.urls import path

app_name = 'e_portal'
urlpatterns = [
    #log
    # path('', log.index, name='index'),
    path('', log.login, name='login'),
    path("main/", log.index, name='index'),
    path("register/", log.register, name='register'),
    path("pwd_reset/", log.pwd_reset, name='pwd_reset'),
    path("error404/", log.Error404, name='error404'),

    #customer
    path("vehicles/", customer.index, name='vehicles_list'),
    # 前端调试使用
    path("vehicles/1/", customer.getVehicleDetails, name='vehicles_detail'),
    # path("vehicles/<int:vehicles_id>/", customer.getVehicleDetails, name='vehicles_detail'),



    #operator



    #manager


]