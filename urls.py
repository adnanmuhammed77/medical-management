from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='homepage'),
    path('appoinment',views.appoinment,name='appoinment'),
    path('signup',views.signup,name='signup'),
    path('medicine',views.medicine,name='medicine'),
    path('booking',views.booking,name='bookingpage'),
    path('sucess',views.sucesspage,name='sucess'),
    path('logout',views.logoutpage,name='logout'),
    path('departments',views.departments,name='dep-page'),
    path('doctors',views.doctorpage,name='doctors'),
    path('career',views.career,name='career'),
    path('about',views.about,name='about'),
    path('academic',views.academic,name='acadpage'),
    path('payment',views.payment,name='payment'),
    path('show',views.showpage,name='show'),
    path('edit',views.edit,name='edit'),
    path('update',views.updatepage,name='update')
    
    
]


