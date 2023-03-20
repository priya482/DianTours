from django.shortcuts import render,redirect
from .forms import myform

# Create your views here.
def dashboard(request):
    context={'pagename':'dashboard'}
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.user.is_authenticated:
        return render(request,'dashboard.html',context)

def profile(request):
    context={'pagename':'profile'}
    return render(request,'profile.html',context)
    
def add_package(request):
    if request.method == 'POST':
        form = myform(request.POST)
        print(form)
        if form.is_valid():
           form.save()
            # Redirect to success page or home page
    else:
        form = myform()
    context={'pagename':'Create Package','form': form}
    return render(request, 'addpackage.html',context)