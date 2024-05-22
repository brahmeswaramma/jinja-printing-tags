from django.shortcuts import render

# Create your views here.
def fun(request):
    d={'name':"blessie","marks":95}
    return render(request,'fun.html',d)