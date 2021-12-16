from django.http import HttpResponse


def index(request):
    return HttpResponse("Mega anime site!")
