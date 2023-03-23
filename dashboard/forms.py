from django import forms
from .models import Packages
#from .models import Customer
from .models import Address

class myform(forms.ModelForm):
    class Meta:
        model=Packages
        # fields=('pkg_id','pkg_title')
        fields = '__all__'
        widgets = {
            'pkg_dec' : forms.Textarea(attrs={'cols': 25,'rows':1.6 ,'class': 'my-custom-class'})
        }        
        #pkg_dec=forms.CharField(widget=forms.Textarea(attrs={'cols': 10,'rows': 10}))
       
 
'''class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['customer_pswd']'''

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'