from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from crud_app.forms import ProgramForm
from crud_app.models import projectdetail


def myhello(request):
    return render(request,'form.html')

def storedata(request):
    form = ProgramForm(request.POST)
    form.save()
    return redirect('hello/showdata')

def showdata(request):
    students = projectdetail.objects.all()
    return render(request,'show.html',{'students':students})

def destroy(request, id):  
    students = projectdetail.objects.get(id=id)  
    students.delete()  
    return redirect("/hello/hello/showdata")

def login(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'reg.html')

# def update(request):
#     return render(request,'edit.html')


def edit(request, id):  
    student = projectdetail.objects.get(id=id)  
    return render(request,'edit.html', {'student': student})  

def update(request, id):  
    student = projectdetail.objects.get(id=id)  
    form = ProgramForm(request.POST, instance=student)  
    if form.is_valid():  
        form.save()  
        return redirect("/hello/hello/showdata")  
        #return HttpResponse('update details')
    return render(request, 'edit.html', {'student': student})  


def search(request):
    # if search.is_valid():  
         
    #     return redirect("/showdata")  
    # return HttpResponse("this is search")
    # query =request.GET['query']
    # student = projectdetail.objects.get(id=id)  
    return render(request,'search.html')

