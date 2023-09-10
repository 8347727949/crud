"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls.static import static

from .views import display_hotel_images,success,hotel_image_view,destroy,edit,update


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('subject1/',views.subject1),
    path('subject_storedata',views.subject_storedata),
    path('subject_showdata',views.subject_showdata),


     path('user_storedata',views.user_storedata),
    path('user_showdata',views.user_showdata),

    path('subject_delete/<int:id>', views.subject_destroy), 
    
    path('subject_edit/<int:id>', views.subject_edit),  
    path('subject_update/<int:id>', views.subject_update),  

    path('user_edit/<int:id>', views.user_edit),  
    path('user_update/<int:id>', views.user_update),  

    path('search',views.search),

    path('image_upload',hotel_image_view,name='image_upload'),
    path('success',success,name='success'),
    path('hotel_images',display_hotel_images,name='hotel_images'),
   
    path('delete/<int:id>', destroy),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>',update),  

    # path('admin_page',views.admin_page),
    # path('signup',views.signup),
    # path('',views.LoginPage),
    # path('',views.home,name='home'),
    path('home',views.home),
    
    # path('logout/',views.LogoutPage),
    # path('main_admin',views.main_admin),
    # Registration
    path('register/', views.register, name='register'),
    # Login and Logout
    path('', views.user_login, name='login'),
     path('home', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),


    path('add_semesters',views.add_semesters,name='add_semesters'), # add semester page
    path('add_semesters_func',views.add_semesters_func,name='add_semesters_func'), # add semester code
    path('view_semesters',views.view_semesters,name='view_semesters'), # view semesters
    path('edit_semesters/<int:semester_id>',views.edit_semesters), # edit semester page
    path('update_semester/<int:semester_id>',views.update_semester), # update semester code 
    path('delete_semester/<int:semester_id>',views.delete_semester), # delete semester code


     path('add_program/' , views.add_program , name="add_program" ), # add program page  
     path('add_program_func',views.add_program_func, name='add_program_func'), # add program code
     path('view_programs',views.view_programs,name='view_programs'), # view program
     path('edit_program/<int:prog_id>',views.edit_program), # edit program page
     path('update_program/<int:prog_id>',views.update_program,name='update_program'), # update program code
     path('delete_program/<int:prog_id>',views.delete_program), # update program code



    path('add_cource',views.add_cource,name='add_cource'), # add semester page
    path('add_cource_func',views.add_cource_func,name='add_cource_func'), # add cource code
    path('view_cource',views.view_cource,name='view_cource'), # view cource
    path('edit_cource/<int:course_id>',views.edit_cource), # edit semester page
    path('update_cource/<int:course_id>',views.update_cource), # update cource code 
    path('delete_cource/<int:course_id>',views.delete_cource), # delete cource code



   

    #  path('hod_login',views.hod_login),
      path('main_admin',views.main_admin),
      path('main_hod',views.main_hod),

     path('add_provisional',views.add_provisional),
      path('store_provisional',views.store_provisional),
       path('show_provisional',views.show_provisional),
       path('delete_provisional/<int:id>',views.delete_provisional),
    path('delete_provisional1/<int:id>',views.delete_provisional1),


       path('add_final_result',views.add_final_result),
       path('store_final_result',views.store_final_result),
       path('show_final_result',views.show_final_result),
       path('delete_final_result/<int:id>',views.delete_final_result),
       path('delete_final_result1/<int:id>',views.delete_final_result1),


       path('add_bonafide',views.add_bonafide),
       path('store_bonafide',views.store_bonafide),
       path('show_bonafide',views.show_bonafide),
       path('delete_bonafide/<int:id>',views.delete_bonafide),
        path('delete_bonafide1/<int:id>',views.delete_bonafide1),

    

    path('demo',views.demo),


    path('send_provisional_request',views.send_provisional_request),
    path('send_final_result_request',views.send_final_result_request),
    path('send_bonafide_request',views.send_bonafide_request),

    path('view_provisional_request',views.view_provisional_request),
    path('view_final_result_request',views.view_final_result_request),
    path('view_bonafide_request',views.view_bonafide_request),



    path('about',views.about),
    path('feedback',views.feedback),
    path('feedback1',views.feedback1),
    path('feedback2',views.feedback2),
    path('feedback3',views.feedback3),
    path('feedback4',views.feedback4),



    path('blog',views.blog),
      path('blog2',views.blog2),

 path('password',views.password),
]
