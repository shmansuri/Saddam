from django.shortcuts import render
from .models import Mymodel

# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request, 'core/index.html', context)

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub= request.POST.get('subject')
        msg=request.POST.get('msg')
        print(name, email, sub, msg)

        data= Mymodel(name=name, email=email, sub=sub, msg=msg)
        data.save()
    context={'contact':'active'}
    return render (request, 'core/contact.html',context)
