from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup



# Add the Cat class & list and view function below the imports


cups = [
  Cup('Lolo', 'foul little demon'),
  Cup('Sachi', 'diluted tortoise shell'),
  Cup('Raven', '3 legged cat')
]




# Create your views here.

#Home View
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

#About View
def about(request):
  return render(request, 'about.html')

def cups_index(request):
  cups = Cup.objects.all()
  return render(request, 'cups/index.html', { 'cups': cups })

def cups_detail(request, cup_id):
    cup = Cup.objects.get(id=cup_id)
    return render(request, 'cups/detail.html', {'cup': cup})