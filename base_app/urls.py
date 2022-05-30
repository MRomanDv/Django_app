from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home, name="home"), #PATH , VIEW (WHAT WILL BE RENDER), TAG
    path('rooms/<str:pk>', views.room, name="room"),  #<> for dinamic routes
    path('create-room/', views.create_room, name="create-room"),
    path('updated-room/<str:pk>/', views.updated_room, name='updated-room'),
    path('delete-room/<str:pk>/',views.delete_Room, name="delete-room"), 
]