from django.shortcuts import render,redirect
from .models import Std,Contact


# Create your views here.
def home(request):
    query = request.GET.get('q','')
    if query:
        std =Std.objects.filter(sname__icontains=query)
    else:
        std = Std.objects.all()    
    
    context = {
        'data':std
    }
    return render(request,'home.html',context)


def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        num = request.POST.get('num')
        course = request.POST.get('course')
        add = request.POST.get('add')
        Std.objects.create(
            sname=name,
            snum=num,
            scourse=course,
            sadd=add
            )
        return redirect('home')
    return render(request,'student.html')
    
    
    

def detils(request,pk):
    student = Std.objects.get(id=pk)
    context = {
        'data':student
    }

    return render(request,'detils.html',context)
    


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            message=message


        )
        return redirect('msg')
        
    return render(request,'contact.html')

def update(request,pk):
    std = Std.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        num = request.POST.get('num')
        course = request.POST.get('course')
        add = request.POST.get('add')
        std.sname=name
        std.snum=num
        std.scourse=course
        std.sadd=add
        std.save()
        return redirect('home')


    context = {
        'std1':std
    }
    return render(request,'update.html',context)


def delete(request,pk):
    std = Std.objects.get(id=pk)
    if request.method == 'POST':
        std.delete()
        return redirect('home')
    context={
        'data': std
    }
    return render(request,'delete.html',context)

def msg(request):
    return render(request,'msg.html')

