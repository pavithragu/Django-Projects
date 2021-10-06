from django.shortcuts import render
from StudentApp.models import Students
from django.shortcuts import redirect
from StudentApp.form import fdetails


# Create your views here.
def check(request):
    details = Students.objects.all()
    details_dict = {"data": details}
    return render(request, 'StudentApp/check.html', context=details_dict)


def create(request):
    store = fdetails()
    data_dict = {'forms': store}
    if request.method == 'POST':
        form = fdetails(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/StudentApp/')
    return render(request, 'StudentApp/create.html', context=data_dict)


def update(request, id):
    details = Students.objects.get(id=id)
    data_dict = {"update": details}
    if request.method == 'POST':
        form = fdetails(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('/StudentApp/')
    return render(request, 'StudentApp/update.html', context=data_dict)


def delete(request, id):
    details = Students.objects.get(id=id)
    details.delete()
    return redirect('/StudentApp/')
