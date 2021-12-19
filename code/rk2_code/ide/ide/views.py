from django.views import generic 

from .models import Ide


class IndexView(generic.ListView):
    template_name = 'ide/index.html'
    context_object_name = 'ides'

    def get_queryset(self):
        ide_instances = Ide.objects.all()

        return ide_instances

