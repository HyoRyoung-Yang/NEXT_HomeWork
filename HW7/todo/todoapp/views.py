from django.shortcuts import render, redirect
from .models import List

# Create your views here.
def home(request):
    lists = List.objects.all().order_by('date')
    
    return render(request, 'home.html', { 'lists' : lists })

def new(request):
    if request.method == 'POST':
        new_list = List.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date']
        )
        return redirect('detail', new_list.pk)
    
    return render(request, 'new.html')

def detail(request, list_pk):
    list = List.objects.get(pk=list_pk)

    return render(request, 'detail.html', { 'list' : list })

def edit(request, list_pk):
    list = List.objects.get(pk=list_pk)

    if request.method == 'POST':
        List.objects.filter(pk=list_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date']
        )
        return redirect('detail', list_pk)

    return render(request, 'edit.html', { 'list' : list })

def delete(request, list_pk):
    list = List.objects.get(pk=list_pk)
    list.delete()

    return redirect('home')