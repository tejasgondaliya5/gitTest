from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('forget/', views.forget_password, name='forget'),
    path('otp/', views.otp, name='otp'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('usersearch/', views.usersearch, name='usersearch'),
    path('applynurse/', views.applynurse, name='applynurse'),
    path('booknurse/<int:A>', views.booknurse, name='booknurse'),
    path('status/', views.status, name='status'),
    path('delete/<int:B>', views.deleteshedule, name='delete'),
    path('addnurse/', views.addnurse, name='addnurse'),
    path('nursedatabase/', views.nursedatabase, name='nursedatabase'),
    path('userdatabase/', views.userdatabase, name='userdatbase'),
    path('detail/', views.nursedetail, name='detail'),
    path('changeShedule/', views.changeShedule, name='changeShedule'),
    path('deletenurse/<int:E>', views.deletenurse, name='deletenurse'),
    path('changedetail/<int:D>', views.changedetail, name='changedetail'),
    path('pationtnotify/', views.pationtnotify, name='alert'),
    path('show/<int:C>', views.show, name='show'),
    path('chackShedule/', views.chack_shedule, name='chackShedule'),
]