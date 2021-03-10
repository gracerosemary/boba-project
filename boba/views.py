from django.shortcuts import render

# ListView, DetailView, DeleteView, CreateView, UpdateView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Boba
from django.urls import reverse_lazy

class BobaListView(ListView):
    template_name = 'boba/boba_list.html'
    model = Boba

class BobaDetailView(DetailView):
    template_name = 'boba/boba_detail.html'
    model = Boba

class BobaCreateView(CreateView):
    template_name = 'boba/boba_create.html'
    model = Boba
    fields = ['drink', 'business', 'description', 'purchaser']
    success_url = reverse_lazy('boba_list')

class BobaUpdateView(UpdateView):
    template_name = 'boba/boba_update.html'
    model = Boba
    fields = ['drink', 'business', 'description', 'purchaser']
    success_url = reverse_lazy('boba_list')

class BobaDeleteView(DeleteView):
    template_name = 'boba/boba_delete.html'
    model = Boba
    success_url = reverse_lazy('boba_list')