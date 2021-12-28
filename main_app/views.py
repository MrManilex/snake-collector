from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
   return render(request, 'base.html')

def about(request):
   return render(request, 'about.html')

def snakes_index(request):
   return render(request, 'snakes/index.html', { 'snakes': snakes })


class Snake:  # Note that parens are optional if not inheriting from another class
   def __init__(self, name, breed, description, age):
      self.name = name
      self.breed = breed
      self.description = description
      self.age = age


snakes = [
   Snake('Lolo', 'tabby', 'Kinda rude.', 3),
   Snake('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
   Snake('Fancy', 'bombay', 'Happy fluff ball.', 4),
   Snake('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]
