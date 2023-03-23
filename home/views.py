from django.shortcuts import render,redirect
from django.contrib import messages


#from dashboard.forms import myform
from dashboard.models import Packages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    context={'pagename':'homepage'}
    return render(request,'index.html',context)

def register(request):
    # context={'page':'hompage'}
    return render(request,'registration.html')

def login(request):
    # pagename = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     # try:
    #     #     user = User.objects.get(email=email)
    #     # except:
    #     #     messages.error(request, 'User does not exist')

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Username OR password does not exit')

    # context = {'pagename': pagename}
    # return render(request, 'login.html', context)
    if request.method == 'POST':
        # return redirect('dashboard')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message="login successfully"
            # context={'pagename':'login','message':message}
            return redirect('home')
        else:
            message="invalid username or password"
            context={'pagename':'login','message':message}
            return redirect('dashboard')
            # Return an error message.
    else:
        message="abcd"
    context={'pagename':'login','message':message}
    return render(request,'login.html',context)

def about(request):
    context={'pagename':'about us'}
    return render(request,'about.html',context)

def contact(request):
    context={'pagename':'contact us'}
    return render(request,'contact.html',context)

def package(request):
    pkgs=Packages.objects.all()
    context={'pagename':'packages','packages':pkgs}
    return render(request,'packages.html',{'pkgs':context})

def packageDetail(request,pkg_id):
    pkg = Packages.objects.filter(id=pkg_id)
    
    context={'pagename': pkg[0].pkg_title,'package':pkg}
    return render(request,'packageDetails.html',context)

'''def add_package(request):
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page or home page
    else:
        form = myform()
    context={'pagename':'Create Package','form': form}
    return render(request, 'addpackage.html',context)
    '''
