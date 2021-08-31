from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post, Contact, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView


# Create your views here.
def Home(request):
    allPost = Post.objects.all().order_by('-timestamp')
    context = {'allposts': allPost}

    return render(request,'index.html', context)

def blog(request, slug):
    post = Post.objects.filter(slug=slug).first()

    # stuff = get_object_or_404(Post, sno=request.POST.get('post_id'))
    # total_likes  = stuff.total_likes()

    # post.like = post.like + 1
    # post.save()

    context = {'post': post}

    return render(request,'blogpost.html', context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<4:
             messages.error(request, 'Please fill the form correctly')
            #  messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(name=name, surname=surname, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request,"Sent")

    return render(request,'contact.html')

def allpost(request):
    return render(request,'allpost.html')

def signup(request):
    if request.method =="POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            confirm = request.POST['confirm']

            # if len(username)<10:
            #      messages.error(request, "Your Username must be 10 characters")
            #      return redirect("/")

            # if not username.isalnum():
            #      messages.error(request, "Your Username shoud only contain letters and numbers")
            #      return redirect("/")

            if password != confirm:
                messages.error(request, "Password do not match")
                return redirect("/")

            #Create User
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect("/")
    else:
        return render(request,'signup.html')

def handelLogin(request):
    if request.method =="POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome to lucicoder {user.username} ")
            return redirect('/')

        else:
            messages.error(request, "Invalid account , please try again")
            return redirect('/')
    return render(request,'login.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logout")
    return redirect('/')


def Likeview(request, pk):
    posts = get_object_or_404(Post, sno=request.POST.get('post_id'))
    posts.likes.add(request.user)
    # return HttpResponse("Liked")
    return HttpResponseRedirect(reverse('Home'))

def robot(request):
    return render(request, 'robots.txt')

# def technology(request, cat):

#     return render(request, 'Category/technology.html', {'cat'})


class CastListView(ListView):
    template_name = 'Category/cate.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':self.kwargs['category'],
            'posts': Post.objects.filter(category=self.kwargs['category'])
        }
        return content


