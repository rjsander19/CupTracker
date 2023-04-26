from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cup

from .forms import UseForm

from django.shortcuts import render, redirect

# Add the Cat class & list and view function below the imports

# cups = [
#   Cup('Lolo', 'foul little demon'),
#   Cup('Sachi', 'diluted tortoise shell'),
#   Cup('Raven', '3 legged cat')
# ]

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
    use_form = UseForm()
    return render(request, 'cups/detail.html', {'cup': cup, 'use_form': use_form})

def add_use(request, cup_id):
    form = UseForm(request.POST)
    if form.is_valid():
       new_use = form.save(commit=False)
       new_use.cup_id = cup_id
       new_use.save()
    return redirect('detail', cup_id=cup_id)

class CupCreate(CreateView):
  model = Cup
  fields = '__all__'
#   success_url = '/cups/'

class CupUpdate(UpdateView):
    model = Cup
    fields = ['description']

class CupDelete(DeleteView):
    model = Cup
    success_url = '/cups/'