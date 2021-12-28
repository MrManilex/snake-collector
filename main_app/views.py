from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.forms import FeedingForm
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
   feeding_form = FeedingForm()
   return render(request, 'snakes/detail.html', { 
      'snake': snake, 'feeding_form': feeding_form })

def add_feeding(request, snake_id):
   form = FeedingForm(request.POST)
   if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.snake_id = snake_id
      new_feeding.save()
   return redirect('snakes_detail', snake_id=snake_id)

class SnakeCreate(CreateView):
   model = Snake
   fields = '__all__'
   success_url = '/snakes/'
   
class SnakeUpdate(UpdateView):
   model = Snake
   fields = ['breed', 'description', 'age']
   
class SnakeDelete(DeleteView):
   model = Snake
   success_url = '/snakes/'