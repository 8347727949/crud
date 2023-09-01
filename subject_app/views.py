from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

from .forms import  *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


from subject_app.forms import subjectForm,Request_provisional_Form
from subject_app.models import subjectdetail,Request_provisional


from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

@login_required(login_url='login')


def subject1(request):
    return render(request,'admin_subject_add.html')

def subject_storedata(request):
    form = subjectForm(request.POST)
    form.save()
    return redirect('/subject_showdata')

def subject_showdata(request):
    students = subjectdetail.objects.all()
    return render(request,'admin_subject_showdata.html',{'students':students})

def subject_destroy(request, id):  
    students = subjectdetail.objects.get(id=id)  
    students.delete()  
    return redirect("/subject_showdata")



# def update(request):
#     return render(request,'edit.html')


def subject_edit(request, id):  
    student = subjectdetail.objects.get(id=id)  
    return render(request,'admin_subject_edit.html', {'student': student})  

def subject_update(request, id):     
    student = subjectdetail.objects.get(id=id)  
    form = subjectForm(request.POST, instance=student)  
    if form.is_valid():  
        form.save()  
        return redirect("/subject_showdata")  
        #return HttpResponse('update details')
    return render(request, 'admin_subject_edit.html', {'student': student})  


def search(request):
    # if search.is_valid():  
         
    #     return redirect("/showdata")  
    # return HttpResponse("this is search")
    # query =request.GET['query']
    # student = projectdetail.objects.get(id=id)  
    return render(request,'search.html')


def home(request):
    return render(request,'home.html')


# def SignupPage(request):
#       return render(request,'register.html')
 
# def SignupPage(request):
#     if request.method=='POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         pass2 = request.POST.get('password1')
        
#         print(uname,email,pass1,pass2)
#         if pass1!=pass2:
#             # return HttpResponse('Wrong Passsword.......!')
#             return render(request,'login.html')
#         else:
#             pass
             
#     else:
            
#             my_user = User.objects.create_user(uname,email,pass1,pass2)
#             my_user.save()
#             #return HttpResponse("user creates successfully.....!")
#             return render(request,'login.html')

#             print(uname,email,pass1,pass2)
                                  
                                  
#     return render(request,'register.html')
# def signup(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect('/')
#     else:
#         form = RegisterForm()
#         # return HttpResponse('hii')
            
        
            

#     return render(request,'registration/register.html',{'form':form})

# def LoginPage(request):
#      if request.method=='POST'  :
#          username = request.POST.get('username')
#          pass22 = request.POST.get('passw')
#          print(username,pass22)
#          user=authenticate(request,username=username,password=pass22) 
#          if (username == "yash" and pass22 == "yash123" ):
#               #return render(request,'admin/')
#             #   if username!=pass22:
#             #     return HttpResponse('Wrong Passsword.......!')
#             #     return render(request,'login.html')
              
#               return render(request,'main_admin.html')
#         #  else:
#         #         messages.warning(request, 'Wrong Username or Password',fail_silently=True)
#         #         return HttpResponseRedirect(request.path_info) 

#          if user is not None: 
#              login(request,user)
#              return render(request,'home.html')
            
#          else:
#               messages.warning(request, 'Wrong Username or Password',fail_silently=True)
#               return HttpResponseRedirect(request.path_info) 
#     #  else:
#     #      user=login()

         
         
         
                                 
         
#      return render(request,'login.html')


# def LogoutPage(request):
#     #  if request.method=='POST':
#          logout(request)
#          return HttpResponse('this is logout page')
        #  messages.success(request,"successfully Logout")
         #return redirect('')
         #return render(request,'login.html')
        
    #return HttpResponse('this is logout page')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/login')
    else:
        form = RegisterForm()
        # return redirect('/login')
            
        
            

    return render(request,'registration/register.html',{'form':form})
    



def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/success')
            
    else:
        form = HotelForm()
    return render(request,'hotel_image_form.html', {'form': form })


def success(request):
    #return HttpResponse('Successfully Upload Image.....!')
    return render(request,'success.html')


def display_hotel_images(request):
    if request.method == 'GET':
       Hotels = Hotel.objects.all()
    return render(request,'display_hotel_images.html',{'hotel_images': Hotels})


def destroy(request, id):  
    hotel = Hotel.objects.get(id=id)  
    hotel.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/hotel_images")


def edit(request, id):  
    hotel = Hotel.objects.get(id=id)  
    return render(request,'edit_image.html', {'hotel':hotel})  

def update(request, id):  
    hotel = Hotel.objects.get(id=id)  
    form = HotelForm(request.POST, request.FILES ,instance = hotel)  
    if form.is_valid():  
        form.save()  
        return redirect("/hotel_images")  
    return render(request, 'edit_image.html', {'hotel': hotel})  

def admin_page(request):
    return render(request,"admin_page.html")

def main_admin(request):
    return render(request,"main_admin.html")



def add_semesters(request):
    program_list = Programmes.objects.all()
    return render(request,'admin_add_semesters.html',{'program_list':program_list})

def add_semesters_func(request):  
    form = SemestersForm(request.POST)
    try:
        sem_data = Semesters.objects.get(semester=request.POST['semester'],prog_id=request.POST['prog_id'])
    except Semesters.DoesNotExist:
        sem_data = None  
    if sem_data:
        messages.warning(request, 'Semester Already Exist For This Course...',fail_silently=True)
        return redirect('add_semesters') 
    else:
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'Semester Added Successfully',fail_silently=True)
                    return redirect('add_semesters')  
                except:  
                    pass  
            else:  
                
                messages.warning(request, 'Semester Not Added...',fail_silently=True)
                return redirect('add_semesters') 
    return render(request,'admin_add_semester.html',{'form':form})

def view_semesters(request):
    semesters_list = Semesters.objects.all().order_by('semester_id')
    program_list = Programmes.objects.all()
    paginator = Paginator(semesters_list, 5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage, Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)  
    return render(request,'admin_view_semesters.html',{'posts':posts,'program_list':program_list}) 

def edit_semesters(request, semester_id):
    semesters_list = Semesters.objects.get(semester_id=semester_id)
    program_list = Programmes.objects.all()
    lst=[1,2,3,4,5,6,7,8,9,10] 
    return render(request,'admin_edit_semesters.html', {'semesters_list':semesters_list,'program_list':program_list,'lst':lst})

def update_semester(request, semester_id):  
    semesters_list = Semesters.objects.get(semester_id=semester_id)
    program_list = Programmes.objects.all()
    lst=[1,2,3,4,5,6,7,8,9,10] 
    form = SemestersForm(request.POST, instance = semesters_list)
    try:
        sem_data = Semesters.objects.get(semester=request.POST['semester'],prog_id=request.POST['prog_id'])
    except Semesters.DoesNotExist:
        sem_data = None  
    if sem_data:
        messages.warning(request, 'Semester Already Exist For This Course...',fail_silently=True)
        return render(request,'admin_edit_semesters.html', {'semesters_list':semesters_list,'program_list':program_list,'lst':lst}) 
    else:  
        if form.is_valid():  
            try:
                form.save()  
                messages.success(request, 'Semester Updated Successfully',fail_silently=True)
                return redirect("view_semesters")
            except:
                pass
        else:
            messages.warning(request, 'Semester Not Updated...',fail_silently=True)
    return render(request, 'admin_edit_semesters.html', {'semesters_list':semesters_list,'program_list':program_list,'lst':lst})


def delete_semester(request, semester_id):  
    semesters_list = Semesters.objects.get(semester_id=semester_id)  
    semesters_list.delete()
    messages.success(request, 'Semester Deleted Successfully',fail_silently=True)  
    return redirect("view_semesters")





def add_program(request):
   # entry_list = Programmes.objects.all()
    return render(request,'admin_add_program.html')

def add_program_func(request):  
    form = ProgramForm(request.POST) 
    try:
        program_data = Programmes.objects.get(program_code=request.POST.get('program_code',False))
    except Programmes.DoesNotExist:
        program_data = None  
    if program_data:
        messages.warning(request, 'program Code Already Exist...',fail_silently=True)
        return HttpResponseRedirect(request.path_info) 
    else: 
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'program Added Successfully',fail_silently=True)
                    return HttpResponseRedirect(request.path_info)  
                except:  
                    pass  
            else:  
                messages.warning(request, 'Program Not Added...',fail_silently=True)
                return HttpResponseRedirect(request.path_info) 
    return render(request,'admin_add_program.html',{'form':form})  

# Function to edit Programs of PhD Department

def edit_program(request, prog_id):
    program_list = Programmes.objects.get(prog_id=prog_id)  
    return render(request,'admin_edit_program.html', {'program_list':program_list})

# Funtion to View all the Programs those exist in PhD Secion

def view_programs(request):
    program_list = Programmes.objects.all().order_by('prog_id')
    paginator = Paginator(program_list, 5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)  
    return render(request,'admin_view_programs.html',{'posts':posts}) 

# Code to update the Program
def update_program(request, prog_id): 
    program_list = Programmes.objects.get(prog_id=prog_id)
    form = ProgramForm(request.POST, instance = program_list) 
    try:
        program_data = Programmes.objects.get(~Q(prog_id=prog_id),program_code=int(request.POST['program_code']))
    except Programmes.DoesNotExist:
        program_data = None  
    if program_data:
        messages.warning(request, 'Program Code Already Exist...',fail_silently=True)
        return render(request, 'admin_edit_program.html', {'program_list':program_list})
    else: 
        if form.is_valid():
            form.save()  
            messages.success(request, 'Program Updated Successfully',fail_silently=True)
            return redirect("view_programs")
    print(form.errors)
    messages.warning(request, 'Programs Not Updated...',fail_silently=True)
    return render(request, 'admin_edit_program.html', {'program_list':program_list})

#code to delete the Program

def delete_program(request, prog_id):  
    program_list = Programmes.objects.get(prog_id=prog_id)  
    program_list.delete()
    messages.success(request, 'Program Deleted Successfully',fail_silently=True)  
    return redirect("view_programs")




def add_cource(request):
   # entry_list = Programmes.objects.all()
    return render(request,'admin_add_cource.html')


def add_cource_func(request):  
    form = CourceForm(request.POST) 
    try:
        cource_data = Cource.objects.get(cource_name=request.POST.get('cource_name',False))
        
    except Cource.DoesNotExist:
        cource_data = None  
    if cource_data:
        messages.warning(request, 'cource Already Exist...',fail_silently=True)
        return HttpResponseRedirect(request.path_info) 
    else: 
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'cource Added Successfully',fail_silently=True)
                    return HttpResponseRedirect(request.path_info)  
                except:  
                    pass  
            else:  
                messages.warning(request, 'cource Not Added...',fail_silently=True)
                return HttpResponseRedirect(request.path_info) 
    return render(request,'admin_add_cource.html',{'form':form})  

# Function to edit Programs of PhD Department

def edit_cource(request, cource_id):
    cource_list = Cource.objects.get(cource_id=cource_id)  
    return render(request,'admin_edit_cource.html', {'cource_list':cource_list})

# Funtion to View all the Programs those exist in PhD Secion

def view_cource(request):
    cource_list = Cource.objects.all().order_by('cource_id')
    paginator = Paginator(cource_list, 5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        posts = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        posts = paginator.page(paginator.num_pages)  
    return render(request,'admin_view_cource.html',{'posts':posts}) 

# Code to update the Program
def update_cource(request,cource_id): 
    cource_list = Cource.objects.get(cource_id=cource_id)
    form = CourceForm(request.POST, instance = cource_list) 
    try:
        cource_data = Cource.objects.get(~Q(cource_id=cource_id),cource_name=str(request.POST['cource_name']))
    except Cource.DoesNotExist:
        cource_data = None  
    if cource_data:
        messages.warning(request, 'cource name Already Exist...',fail_silently=True)
        return render(request, 'admin_edit_cource.html', {'cource_list':cource_list})
    else: 
        if form.is_valid():
            form.save()  
            messages.success(request, 'cource Updated Successfully',fail_silently=True)
            return redirect("view_cource")
    print(form.errors)
    messages.warning(request, 'cource Not Updated...',fail_silently=True)
    return render(request, 'admin_edit_cource.html', {'cource_list':cource_list})

#code to delete the Program

def delete_cource(request, cource_id):  
    cource_list = Cource.objects.get(cource_id=cource_id)  
    cource_list.delete()
    messages.success(request, 'cource Deleted Successfully',fail_silently=True)  
    return redirect("view_cource")




def send_provisional_request(request):
    return render(request,"send_provisional_request.html")

def send_final_result_request(request):
    return render(request,"send_final_result_request.html")

def send_bonafide_request(request):
    return render(request,"send_bonafide_request.html")



def view_provisional_request(request):
    return render(request,"view_provisional_request.html")

def view_final_result_request(request):
    return render(request,"view_final_result_request.html")

def view_bonafide_request(request):
    return render(request,"view_bonafide_request.html")





# HOD LOGIN


def hod_login(request):
    # return render(request,"hod_login.html")
    if request.method=='POST'  :
         hod_username = request.POST.get('username1')
         hod_pass22 = request.POST.get('passw1')
         print(hod_username,hod_pass22)
         user=authenticate(request,username=hod_username,password=hod_pass22) 
         if (hod_username == "hod" and hod_pass22 == "1234" ):
            
              
            #   return render(request,'show_provisional.html')
            return redirect('/show_provisional')
         else:
             messages.warning(request, 'Wrong Username or Password',fail_silently=True)
             return HttpResponseRedirect(request.path_info) 
            #  return render(request,'hod_login.html')
             
             
    else:
     return render(request,'hod_login.html')
    
def admin_login(request):
    # return render(request,"hod_login.html")
    if request.method=='POST'  :
         admin_username = request.POST.get('username')
         admin_pass22 = request.POST.get('password')
         print(admin_username,admin_pass22)
         user=authenticate(request,username=admin_username,password=admin_pass22) 
         if (admin_username == "admin@3492" and admin_pass22 == "yash@2411" ):
            
              
            # return render(request,'main_admin.html')
            return redirect('main_admin')
            
         else:
             messages.warning(request, 'Wrong Username or Password',fail_silently=True)
             return HttpResponseRedirect(request.path_info) 
            #  return render(request,'hod_login.html')
             
             
    else:
     return render(request,'hod_login.html')
    

def add_provisional(request):
    
     return render(request,'send_provisional_request.html')
     

         
def store_provisional(request):
  
    form = Request_provisional_Form(request.POST) 
    try:
        student_data = Request_provisional.objects.get(enrollment=request.POST.get('enrollment',False))
        messages.success(request, 'Request Send Successfully',fail_silently=True) 
    except Request_provisional.DoesNotExist:
        student_data = None  
    if student_data:
        messages.warning(request, 'Request Already Exist...',fail_silently=True)
        return HttpResponseRedirect(request.path_info) 
    else: 
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'Request send Successfully',fail_silently=True)
                    return HttpResponseRedirect(request.path_info)  
                except:  
                    pass  
            else:  
                messages.warning(request, 'Request Not Added...',fail_silently=True)
                return HttpResponseRedirect(request.path_info) 
    return render(request,'show_provisional.html',{'form':form})  
    #return redirect('/add_provisional')
    


def show_provisional(request):
    # students=Request_provisional.objects.all()
    # return render(request,'show_provisional.html',{'students':students})
    request_list = Request_provisional.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    return render(request,'hod_view_provisional_request.html',{'students':students})
    return render(request,'view_provisional_request.html',{'students':students})

def view_provisional_request(request):
    # students=Request_provisional.objects.all()
    # return render(request,'show_provisional.html',{'students':students})
    request_list = Request_provisional.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    # return render(request,'hod_view_provisional_request.html',{'students':students})
    return render(request,'view_provisional_request.html',{'students':students})



def delete_provisional(request, id):  
    program_list = Request_provisional.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/show_provisional")

def delete_provisional1(request, id):  
    program_list = Request_provisional.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/view_provisional_request")



def add_final_result(request):
    return render(request,'send_final_result_request.html')
     

         
def store_final_result(request):
    form = Request_final_result_Form(request.POST) 

    try:
        student_data = Request_final_result.objects.get(enrollment=request.POST.get('enrollment',False))
        messages.success(request, 'Request Send Successfully',fail_silently=True) 
    except Request_final_result.DoesNotExist:
        student_data = None  
    if student_data:
        messages.warning(request, 'Request Already Exist...',fail_silently=True)
        return HttpResponseRedirect(request.path_info) 
    else: 
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'Request send Successfully',fail_silently=True)
                    return HttpResponseRedirect(request.path_info)  
                except:  
                    pass  
            else:  
                messages.warning(request, 'Request Not Added...',fail_silently=True)
                return HttpResponseRedirect(request.path_info) 
    #return render(request,'show_provisional.html',{'form':form})  
    return redirect('/add_final_result')
    


def show_final_result(request):
    # students=Request_final_result.objects.all()
    # return render(request,'hod_view_final_result_request.html',{'students':students})
    request_list = Request_final_result.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    return render(request,'hod_view_final_result_request.html',{'students':students})


def view_final_result_request(request):
    request_list = Request_final_result.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    return render(request,'view_final_result_request.html',{'students':students})


def delete_final_result(request, id):  
    program_list = Request_final_result.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/show_final_result")

def delete_final_result1(request, id):  
    program_list = Request_final_result.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/view_final_result_request")







def add_bonafide(request):
    return render(request,'send_bonafide_request.html')
     

def store_bonafide(request):
    form = Request_bonafide_Form(request.POST) 
    try:
        student_data = Request_bonafide.objects.get(enrollment=request.POST.get('enrollment',False))
        messages.success(request, 'Request Send Successfully',fail_silently=True) 
    except Request_bonafide.DoesNotExist:
        student_data = None  
    if student_data:
        messages.warning(request, 'Request Already Exist...',fail_silently=True)
        return HttpResponseRedirect(request.path_info) 
    else: 
        if request.method == "POST":   
            if form.is_valid():  
                try:  
                    form.save()
                    messages.success(request, 'Request send Successfully',fail_silently=True)
                    return HttpResponseRedirect(request.path_info)  
                except:  
                    pass  
            else:  
                messages.warning(request, 'Request Not Added...',fail_silently=True)
                return HttpResponseRedirect(request.path_info) 
    #return render(request,'show_provisional.html',{'form':form})  
    return redirect('/add_bonafide')
    


def show_bonafide(request):
    # students=Request_final_result.objects.all()
    # return render(request,'hod_view_bonafide_request.html',{'students':students})
    request_list = Request_bonafide.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    return render(request,'hod_view_bonafide_request.html',{'students':students})


def view_bonafide_request(request):
    request_list = Request_bonafide.objects.all().order_by('enrollment')
    paginator = Paginator(request_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        students = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        students = paginator.page(paginator.num_pages)  
    return render(request,'view_bonafide_request.html',{'students':students})



def delete_bonafide(request, id):  
    program_list = Request_bonafide.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/show_bonafide")

def delete_bonafide1(request, id):  
    program_list = Request_bonafide.objects.get(id=id)  
    program_list.delete()
    messages.success(request, 'Request Deleted Successfully',fail_silently=True)  
    return redirect("/view_bonafide_request")



def demo(request):
     return render(request,'demo.html')

def main_hod(request):
     return render(request,'main_hod.html')


