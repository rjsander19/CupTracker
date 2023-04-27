from django.views.generic import ListView, DetailView

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cup, Content

from .forms import UseForm

from django.shortcuts import render, redirect



# cups = [
#   Cup('Lolo', 'foul little demon'),
#   Cup('Sachi', 'diluted tortoise shell'),
#   Cup('Raven', '3 legged cat')
# ]



#Home View
def home(request):
  return HttpResponse('<h1>Welcome to Cup Collector! </h1>')

#About View
def about(request):
  return render(request, 'about.html')

@login_required
def cups_index(request):
  cups = Cup.objects.filter(user=request.user)
  return render(request, 'cups/index.html', { 'cups': cups })

@login_required
def cups_detail(request, cup_id):
    cup = Cup.objects.get(id=cup_id)

    contents_cup_doesnt_have = Content.objects.exclude(id__in = cup.contents.all().values_list('id'))
    cup.contents.all().values_list('id')

    use_form = UseForm()
    return render(request, 'cups/detail.html', {'cup': cup, 'use_form': use_form, 'contents': contents_cup_doesnt_have})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def add_use(request, cup_id):
    form = UseForm(request.POST)
    if form.is_valid():
       new_use = form.save(commit=False)
       new_use.cup_id = cup_id
       new_use.save()
    return redirect('detail', cup_id=cup_id)


@login_required
def assoc_content(request, cup_id, content_id):
  Cup.objects.get(id=cup_id).contents.add(content_id)
  return redirect('detail', cup_id=cup_id)



class CupCreate(LoginRequiredMixin, CreateView):
  model = Cup
  fields = ('name', 'description')
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CupUpdate(LoginRequiredMixin, UpdateView):
    model = Cup
    fields = ['description']

class CupDelete(LoginRequiredMixin, DeleteView):
    model = Cup
    success_url = '/cups/'



class ContentsIndex(LoginRequiredMixin, ListView):
    model = Content

class ContentsDetail(LoginRequiredMixin, DetailView):
    model = Content

class ContentCreate(LoginRequiredMixin, CreateView):
    model = Content
    fields = '__all__'

class ContentUpdate(UpdateView):
    model = Content
    fields = '__all__'

class ContentDelete(LoginRequiredMixin, DeleteView):
    model = Content
    success_url = '/contents/'