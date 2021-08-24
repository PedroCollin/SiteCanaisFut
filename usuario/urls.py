from django.urls import path
from . import views

urlpatterns =[
    path('',views.login,name='index_login'),
    path('login/',views.login,name='index_login'),
    path('logout/',views.logout,name='index_login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('dashboard/',views.dashboard,name='index_login')
]