from django.shortcuts import render,redirect
from .forms import myform
#from .forms import CustomerForm
from .forms import AddressForm
from django.contrib import messages
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
        messages.success(request, 'Data submitted successfully!')
            # Redirect to success page or home page
    else:
        form = myform()
    context={'pagename':'Create Package','form': form}
    return render(request, 'addpackage.html',context)



'''def add_customer(request):
    if request.method=='POST':
        form = CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully!')
    else:
        form=CustomerForm()
    context={'pagename':'Add customer','form': form}
    return render(request,'addcustomer.html',context)'''

def add_address(request):
    if request.method=='POST':
        form = AddressForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully!')
    else:
        form=AddressForm()
        
    context={'pagename':'Add customer','form': form}
    return render(request,'address.html',context)