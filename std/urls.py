from django.urls import path
from . import views



urlpatterns = [
   
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('detils/<int:pk>',views.detils,name='detils'), 
    path('update/<int:pk>',views.update,name='update'),
    path('student',views.student,name='student'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('msg',views.msg,name='msg'),

]