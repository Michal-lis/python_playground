from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')#render patrzy domyślnie w templates directory

def contact(request):
    return render(request,'personal/contact.html')
