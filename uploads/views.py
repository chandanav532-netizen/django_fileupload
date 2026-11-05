from django.shortcuts import render, redirect 
from .forms import DocumentForm 
from .models import document
def upload_file(request):  
    if request.method == 'POST':        
          form = DocumentForm(request.POST, request.FILES)       
          if form.is_valid():            
              form.save()                   
              return redirect('upload_success')    
    else:        
        form = DocumentForm()    
    return render(request, 'uploads/upload.html', {'form': form}) 
def upload_success(request):   
     return render(request, 'uploads/success.html') 
def document_list(request):    
    documents = document.objects.all().order_by('-uploaded_at')    
    return render(request, 'uploads/list.html', {'documents': documents})