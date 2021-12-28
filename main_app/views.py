from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Snake

# Create your views here.

def home(request):
   return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def snakes_index(request):
   snakes = Snake.objects.all()
   return render(request, 'snakes/index.html', { 'snakes': snakes })

def snakes_detail(request, snake_id):
   snake = Snake.objects.get(id=snake_id)
   return render(request, 'snakes/detail.html', { 'snake': snake })

class SnakeCreate(CreateView):
   model = Snake
   fields = '__all__'
   success_url = '/snakes/'