from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.
class SnacksListView(ListView):
    template_name='snakslist.html'
    model = Snack

class SnacksDetailView(DetailView):
    template_name='snaksdetail.html'
    model = Snack

class SnacksCreateView(CreateView):
    template_name='createsnaks.html'
    model = Snack
    fields = ['title','purchaser','description']

class SnacksDeleteView(DeleteView):
    template_name='deletesnaks.html'
    model = Snack
    success_url = reverse_lazy('snakslist')

class SnacksUpdateView(UpdateView):
    template_name='updatesnaks.html'
    model = Snack
    fields = ['title','description']
    success_url = reverse_lazy('snakslist')