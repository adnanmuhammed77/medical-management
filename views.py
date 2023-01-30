from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import product,Booking
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request,'home.html')
def appoinment(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if  user is not None:
             login(request,user)
             return redirect('bookingpage')
        else:
            # return HttpResponse("username or password is incorrect")
             messages.error(request,'invalid username and password!!!')
    return render(request,'appoinment.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            # return HttpResponse("your passoword and conform password are not same")
            messages.error(request,'password and conform password are not same! ')
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('appoinment')
    return render(request,'signup.html')
def medicine(request):
    pro=product.objects.all()
    return render(request,'medicine.html',{'products':pro})
def booking(request):
    if  request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)  

def sucesspage(request):
    return render(request,'sucess.html')
def logoutpage(request):
    logout(request)
    return redirect('homepage')
def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
def doctorpage(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def career(request):
    return render(request,'career.html')

def about(request):
    return render(request,'about.html')
def academic(request):
    return render(request,'academic.html')
def payment(request):
    return render(request,'payment.html')
def showpage(request):
    show = Booking.objects.all()
    return render(request,'show.html',{'update':show})
def edit(request,id):
    patient =Booking.objects.get(id=id)
    return render(request,'edit.html',{'patients':patient})
def updatepage(request, id):  
    patient = Booking.objects.get(id=id)  
    form = BookingForm(request.POST, instance = patient)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'patients': patient})

  