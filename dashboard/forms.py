from django import forms
from .models import Packages

class myform(forms.ModelForm):
    class Meta:
        model=Packages
        # fields=('pkg_id','pkg_title')
        fields='__all__'
 