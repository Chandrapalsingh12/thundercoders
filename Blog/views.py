from django.shortcuts import render, HttpResponse
from .models import Post, Contact
from django.contrib import messages


# Create your views here.
def Home(request):
    allPost = Post.objects.all()
    context = {'allposts': allPost}
    
    return render(request,'index.html', context)

def blog(request, slug):
    post = Post.objects.filter(slug=slug).first()   
    
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
