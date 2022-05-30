from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context 
from .models import Room, Topic #IMPORT ROOM MODEL TO MAKE A QUERY 
from .forms import RoomForm
# Create your views here.

rooms = [
    {'id':1, 'name':'learning django'},
    {'id':2, 'name':'learn about Models'},
    {'id':3, 'name':'learn about Migrations, classes and methods'},
]

def home(request):
    rooms = Room.objects.all() #variable = Model.objectManager.method THIS IS A QUERY

    topic = Topic.objects.all()
    context = {'rooms_list':rooms, 'topics':topic}
    return render(request, 'base_app/home.html', context ) 

def room(request,pk): 
    """room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i """
    room = Room.objects.get(id=pk)#THIS IS A QUERY , GET WILL RETURN A SINGLE ITEM not more        
    context = {"room_list":room}        
    return render(request, 'base_app/room.html',context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST) # request.post is the inserted data in the roomform in room_form.html
        if form.is_valid: #if type of value, max length,null = True or False is valid acording to the Model
            form.save() #this will save in the DB
            return redirect('home') #home is allowed this be written just like that buecause of the tag name="home" in the urls.py  
    context = {'form':form}
    return render(request, 'base_app/room_form.html',context)


def updated_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #meaning this form will be pre-filled with the <room> value
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room) #in second parameter had specify wich room will be updated 
        if form.is_valid:
            form.save()
            return redirect('home') 
    context = {'form':form}
    return render(request, 'base_app/room_form.html',context)

def delete_Room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request,'base_app/delete.html',{'obj':room})      

