from django.urls import path
from mineapp  import  views


urlpatterns=[
    path('',views.home,name='home'),
    path('abt/', views.abt, name='abt'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.serv, name='servic'),
    path('blog/', views.heo, name='blo'),
    path('assignment/', views.assin, name='assi'),
]