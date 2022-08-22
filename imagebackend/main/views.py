from django.shortcuts import render
from .models import Images,Catrgory

def Home(request):
    img=Images.objects.all()
    list=Catrgory.objects.all()
    context={'img':img,'list':list}
    return render(request, 'home.html',context)
