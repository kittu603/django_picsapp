from django.urls import path
from . import views

app_name = 'photoapp'   #this is useful when someother app in this pro has same name ='detail', called as namespaces


urlpatterns = [
    path('', views.index , name = 'index'),
    path('<int:pk>/', views.detail , name = 'detail')
]
