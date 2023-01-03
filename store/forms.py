from django import forms
from django.forms import BaseForm

from .models import  Company, staffManagement, DropStaff, stockCategory,stockSubCategory,Stock

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['code', 'name','address','email']
        widgets = {
            'code':forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'code',
        'data-val': 'true',
        'data-val-required': 'Please enter code',
        }),
        'name': forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }),
        'address': forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }),
        'email':forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }),
    }

# dropForm
class DropStaffForm(forms.ModelForm):
    class Meta:
        model = DropStaff
        fields = ['role']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control', 'id': 'role'})
        }


# staff form
class StaffForm(forms.ModelForm):
    class Meta:
        model = staffManagement
        fields = ['code','first_name', 'last_name', 'email','drop']

        widgets = {
            'code':forms.TextInput(attrs={'class': 'form-control','id': 'code'}),
           
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'drop': forms.Select(attrs={'class': 'form-control', 'id': 'drop'}),

            
        }

# stock  
class StockCategoryForm(forms.ModelForm):
    class Meta:
        model=stockCategory
        fields = ['category']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'id': 'category'})
        }

class StockSubCategoryForm(forms.ModelForm):
    class Meta:
        model=stockSubCategory
        fields = ['category','sub_category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category'}),
            'sub_category': forms.TextInput(attrs={'class': 'form-control', 'id': 'sub_category'})
        }

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['code','name','alias_name','price','quantity','total','category','sub_category']
        widgets={
            'code':forms.TextInput(attrs={'class': 'form-control','id': 'code'}),
           
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'alias_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'alias_name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'id': 'price'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'id': 'total'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category'}),
            'sub_category': forms.Select(attrs={'class': 'form-control', 'id': 'sub_category'}),
            
            
            
        }

class StockSearchForm(forms.ModelForm):
    pass
            
          
 
    
# class BuyerForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))
   

# class BuyerForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))

