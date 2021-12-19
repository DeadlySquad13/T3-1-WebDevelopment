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


def update(request, ide_id):
    ide = get_object_or_404(Ide, pk=ide_id)

    try:
        selected_language = ide.programming_languages.get(pk=request.POST['selected_language'])
    except (KeyError, ProgrammingLanguage.DoesNotExist):
        # Redisplay the ide voting form.
        return render(request, 'ide/detail.html', {
            'ide': ide,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_language.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ide/detail.html', args=(ide.id,)))


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


