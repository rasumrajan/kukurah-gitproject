from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.dogs, name='dogs'),
    path('<int:id>', views.dog_detail, name='dog_detail'),
    path('search', views.search,name='search'),
    

]

