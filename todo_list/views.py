from django.shortcuts import render, redirect
from .models import *
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request, "Item has been added successfully")
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item has been deleted successfully !")
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Item has been editted successfully")
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


def about(request):
    name = 'Abdur RAHMAN'
    designation = 'programmer'
    descriptipon = 'Sometime about myself/sompany..Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'

    return render(request, 'about.html', {'name': name, 'designation': designation, 'descriptipon': descriptipon,})
