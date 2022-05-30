from tkinter.tix import Form
from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta: #class Meta as the metadata of model Room
        model = Room 
        fields = '__all__' #catch the inserted data of all the fields in Room Model