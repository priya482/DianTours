from django.shortcuts import render,redirect
from django.contrib import messages


#from dashboard.forms import myform
from django.http import HttpResponse
from dashboard.models import Packages,Agent,Address
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    context={'pagename':'homepage'}
    return render(request,'index.html',context)

def register(request):
    # context={'page':'hompage'}
    return render(request,'registration.html')


def registerAgent(request):
    
    context={'pagename':'registration'}
    return render(request,'registration.html',context)
    return HttpResponse("Agent registration successful")
    
'''if request.method == 'POST':
        agency_name = request.POST.ge t('agencyname')
        agent_name = request.POST.get('name')
        agent_email = request.POST.get('email')
        agent_cno = request.POST.get("contact")
        agent_gender = request.POST.get('gender') 
        agent_dob = request.POST.get('dob')
        add_no= request.POST.get('houseno') 
        add_street= request.POST.get('appartment') 
        add_city = request.POST.get('city')
        add_zip = request.POST.get('zipcode')
        add_country = request.POST.get('country')
        add_state = request.POST.get('state')
        agent_pswd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')

        if agent_pswd == cpwd:
            agent_add = Address(add_no=add_no,add_state=add_state,add_street=add_street,add_country=add_country,add_city=add_city,add_zip=add_zip)
            agent_add.save()
            agent = Agent(agency_name=agency_name,agent_pswd=agent_pswd,agent_gender=agent_gender, agent_name=agent_name,agent_email=agent_email,agent_add=agent_add,agent_cno=agent_cno,agent_dob=agent_dob)
            agent.save()
            '''


def login_user(request):
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
            return redirect('/dashboard')
            # Return an error message.
    else:
        message="abcd"
    context={'pagename':'login','message':message}
    return render(request,'login_user.html',context)

def about(request):
    context={'pagename':'about us'}
    return render(request,'about.html',context)

def contact(request):
    context={'pagename':'contact us'}
    return render(request,'contact.html',context)

def package(request):
    pkgs=Packages.objects.all()
    context={'pagename':'packages','packages':pkgs}
    return render(request,'packages.html',{'context':context})

def packageDetail(request,id):
    pkg = Packages.objects.filter(id=id)
    context={'pagename': pkg[0].pkg_title,'package':pkg[0]}
    return render(request,'packageDetails.html',{'context':context})

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
def agentLogin(request):
   print(request)
   return render(request, 'dashboard.html')

def checkAgent(request):
    if request.method == 'POST':
        # return redirect('dashboard')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message="login successfully"
            # context={'pagename':'login','message':message}
            return redirect('dashboard')
        else:
            message="invalid username or password"
            context={'pagename':'login','message':message}
            return redirect('/agentLogin')
            # Return an error message.
    else:
        message="abcd"
        context={'pagename':'login','message':message}
        return render(request,'checkAgent.html',context)