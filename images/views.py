from django.shortcuts import render  ,HttpResponse
from images.forms import UserImageForm  
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
    else:  
        return HttpResponse("sorry,,,,,")
  
    return render(request, 'image_form.html', {'form': form})  

