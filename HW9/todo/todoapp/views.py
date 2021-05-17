from django.shortcuts import render, redirect
from .models import List, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    lists = List.objects.all().order_by('date')

    return render(request, 'home.html', {'lists': lists})


@login_required (login_url="/registration/login")
def new(request):
    if request.method == 'POST':
        new_list = List.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date'],
            author = request.user
        )
        return redirect('detail', new_list.pk)

    return render(request, 'new.html')


def detail(request, list_pk):
    list = List.objects.get(pk=list_pk)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            list=list,
            content=content,
            author = request.user
        )
        return redirect('detail', list_pk)

    return render(request, 'detail.html', {'list': list})


def edit(request, list_pk):
    list = List.objects.get(pk=list_pk)

    if request.method == 'POST':
        List.objects.filter(pk=list_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date']
        )
        return redirect('detail', list_pk)

    return render(request, 'edit.html', {'list': list})


def delete(request, list_pk):
    list = List.objects.get(pk=list_pk)
    list.delete()

    return redirect('home')


def delete_comment(request, list_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', list_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if(len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})
        
        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )

        auth.login(request, new_user)
        return redirect('home')
    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(request, found_user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect('home')
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def mypage(request, user_pk):
    user = User.objects.get(pk=user_pk)
    lists = user.lists.all().order_by('date')
    comments = user.comments.all()

    return render(request, 'mypage.html', {'user':user ,'lists': lists, 'comments':comments})
