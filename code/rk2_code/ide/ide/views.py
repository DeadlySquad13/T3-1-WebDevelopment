from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)

from .models import Ide, ProgrammingLanguage


class IndexView(ListView):
    template_name = 'ide/index.html'
    context_object_name = 'ides'

    def get_queryset(self):
        ide_instances = Ide.objects.all()

        return ide_instances


class DetailView(DetailView):
    model = Ide
    template_name = 'ide/detail.html'


modifiableIdeFields = ['title', 'price', 'programming_languages']


class IdeCreateView(CreateView):
    model = Ide
    template_name = 'ide/ide_create.html'
    fields = modifiableIdeFields


class IdeUpdateView(UpdateView):
    model = Ide
    template_name = 'ide/ide_update.html'
    fields = modifiableIdeFields


class IdeDeleteView(DeleteView):
    model = Ide
    template_name = 'ide/ide_delete.html'

    # User won't be redirected until delete operation finishes.
    success_url = reverse_lazy('index')


