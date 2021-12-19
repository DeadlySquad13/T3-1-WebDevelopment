from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic 

from .models import Ide, ProgrammingLanguage


class IndexView(generic.ListView):
    template_name = 'ide/index.html'
    context_object_name = 'ides'

    def get_queryset(self):
        ide_instances = Ide.objects.all()

        return ide_instances


class DetailView(generic.DetailView):
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




# def emp(request):  
    # if request.method == "POST":
        # form = EmployeeForm(request.POST)
        # if form.is_valid():
            # try:
                # form.save()
                # return redirect('/show')
            # except:
                # pass
    # else:
        # form = EmployeeForm()
    # return render(request,'index.html',{'form':form})
# def show(request):
    # employees = Employee.objects.all()
    # return render(request,"show.html",{'employees':employees})
# def edit(request, id):
    # employee = Employee.objects.get(id=id)
    # return render(request,'edit.html', {'employee':employee})
# def update(request, id):
    # employee = Employee.objects.get(id=id)
    # form = EmployeeForm(request.POST, instance = employee)
    # if form.is_valid():  
        # form.save()  
        # return redirect("/show")  
    # return render(request, 'edit.html', {'employee': employee})
# def destroy(request, id):
    # employee = Employee.objects.get(id=id)
    # employee.delete()
    # return redirect("/show")
