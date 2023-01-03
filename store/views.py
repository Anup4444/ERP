from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
# from users.models import User
from django.db.models import Q
# from .decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import render, redirect
# from .models import RolesManagement


# from django.contrib.auth.models import Permission, User, Group
# from django.contrib.contenttypes.models import ContentType
# from django.http import HttpResponse

from .models import (
    
    Company,
    staffManagement,
    DropStaff,
    stockCategory,
    stockSubCategory,
    Stock,
    
)
from .forms import (
    
    CompanyForm,
    StaffForm,
    DropStaffForm,
    StockCategoryForm,
    StockSubCategoryForm,
    StockForm,
)
# CompanyView


# @login_required(login_url='login')
# def roles(request):
#     if request.method == "GET":
#         return render(request, 'store/roles.html')
    
#     if request.method == "POST":
#         roles = RolesManagement.objects.all()
#         num = roles.count() + 100
        
#         name = request.POST['name']
#         role_id = request.POST['ROL_ID']
        
#         role_id = role_id + str(num)
        
#         RolesManagement(name=name, role_id=role_id).save()
        
#         return redirect('dashboard')
        
        

# def users(request):
#     return render(request, 'staffmanagement/usercreation.html')


# def permission(request):
#     user = User.objects.all()
#     stock = ContentType.objects.get_for_model(Stock)
#     stock_perms = Permission.objects.filter(content_type=stock)
  
#     data = {
#         'stock_perms':stock_perms,
        
#     }
    
#     if request.method == "POST":
#         selected_permissions = request.POST.getlist('permissions[]')
#         group_name = request.POST['name']
        
#         roles = RolesManagement.objects.all()
#         num = roles.count() +100
        
#         role_id = "ROL" + str(num)
        
#         group, created = Group.objects.get_or_create(name=group_name)
        
#         if not created:
#             return HttpResponse("Group not created")
        
#         else:
#             role = RolesManagement.objects.create(name=group_name, group=group, role_id=role_id)
#             for perm in selected_permissions:
#                 role.group.permissions.add(perm)
#         return redirect('permissions')
            
#     return render(request, 'store/perms.html', data)


@login_required(login_url='login')
def create_company(request):
    forms = CompanyForm()
    if request.method == 'POST':
        forms = CompanyForm(request.POST)
        if forms.is_valid():
            cd=forms.cleaned_data
            pc=Company(
                code=cd['code'],
                name=cd['name'],
                address=cd['address'],
                email=cd['email'],
            )
            pc.save()
            return redirect('company-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCompany.html', context)

class CompanyListView(ListView):
    model = Company
    template_name = 'store/company_list.html'
    context_object_name = 'company'


@login_required(login_url='login')   
def update_company(request,pk):
    if request.method == 'POST':
        cp=Company.objects.get(pk=pk)
        form=CompanyForm(request.POST, instance=cp)
        if form.is_valid():
            cd=form.cleaned_data
            pc=Company(
                code=cd['code'],
                name=cd['name'],
                address=cd['address'],
                email=cd['email'],
            )
            pc.save()
            return redirect('company-list')
    else:
        cp=Company.objects.get(pk=pk)
        form=CompanyForm(instance=cp)
    
    return render(request,'store/updateCompany.html',{'form':form})

@login_required(login_url='login')  
def delete_company(request,pk):
    if request.method == 'POST':
        company=Company.objects.get(pk=pk)
        company.delete()
        return redirect('company-list')
    
# staff views
@login_required(login_url='login')
def create_staff(request):
    forms = StaffForm()
    if request.method == 'POST':
        forms = StaffForm(request.POST)
        if forms.is_valid():
            code = forms.cleaned_data['code']
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            email = forms.cleaned_data['email']
            drop=forms.cleaned_data['drop']
            # user = User.objects.create_user(username=first_name, last_name=last_name, email=email, is_staffs=True)
           
            staffManagement.objects.create(
                
                code=code,
                first_name=first_name,
                last_name=last_name,
                email=email,
                drop=drop,
                
                
            )
            return redirect('staff-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addStaff.html', context)


class StaffListView(ListView):
    model = staffManagement
    template_name = 'store/staff_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = staffManagement.objects.all().order_by('-pk')
        return context
 
@login_required(login_url='login')   
def update_staff(request,pk):
    if request.method == 'POST':
        cp=staffManagement.objects.get(pk=pk)
        form=StaffForm(request.POST, instance=cp)
        if form.is_valid():
            form.save()
            return redirect('staff-list')
    else:
        cp=staffManagement.objects.get(pk=pk)
        form=StaffForm(instance=cp)
    
    return render(request,'store/updateStaff.html',{'form':form})

@login_required(login_url='login')  
def delete_staff(request,pk):
    if request.method == 'POST':
        staff=staffManagement.objects.get(pk=pk)
        staff.delete()
        return redirect('staff-list')   
    
    
# Dropstaff views
@login_required(login_url='login')
def create_drop_staff(request):
    forms = DropStaffForm()
    if request.method == 'POST':
        forms = DropStaffForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-staff')
    context = {
        'form': forms
    }
    return render(request, 'store/addDropStaff.html', context)


# @login_required(login_url='login')
# def add_staff_group(request):
#     forms=StaffForm()
#     if request.method== 'POST':
#         forms=StaffForm(request.POST)
#         if forms.is_valid():
#             drop=forms.cleaned_data['drop']
#             gname=Group.objects.get(name=drop)
            
            
        
        


# Stock
@login_required(login_url='login')
def create_stock(request):

    forms = StockForm()
    if request.method == 'POST':
        forms = StockForm(request.POST)
        if forms.is_valid():
            code = forms.cleaned_data['code']
            name = forms.cleaned_data['name']
            alias_name = forms.cleaned_data['alias_name']
            price = forms.cleaned_data['price']
            quantity=forms.cleaned_data['quantity']
            total=forms.cleaned_data['total']
            category=forms.cleaned_data['category']
            sub_category=forms.cleaned_data['sub_category']
            Stock.objects.create(
                code=code,
                name=name,
                alias_name=alias_name,
                price=price,
                quantity=quantity,
                total=total,
                category=category,
                sub_category=sub_category,
                
                
            )
            return redirect('stock-list')
    context = {
        'form': forms,
       
    }
    return render(request, 'store/addStock.html', context)


class StockListView(ListView):
    model = Stock
    template_name = 'store/stock_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock'] = Stock.objects.all().order_by('-pk')
        return context
 
@login_required(login_url='login') 

def update_stock(request,pk):
    if request.method == 'POST':
        cp=Stock.objects.get(pk=pk)
        form=StockForm(request.POST, instance=cp)
        if form.is_valid():
            form.save()
            return redirect('stock-list')
    else:
        cp=Stock.objects.get(pk=pk)
        form=StockForm(instance=cp)
    
    return render(request,'store/updateStock.html',{'form':form})

@login_required(login_url='login')   
def delete_stock(request,pk):
    if request.method == 'POST':
        stock=Stock.objects.get(pk=pk)
        stock.delete()
        return redirect('stock-list') 
  

@login_required(login_url='login')  
def stock_search(request):
    if request.method== "GET":
        search=request.GET.get('search')
        search_out=Stock.objects.filter(Q(name__icontains=search)|
                                        Q(alias_name__icontains=search)|
                                        Q(code__icontains=search)|
                                        Q(price__icontains=search)|
                                        Q(quantity__icontains=search)|
                                        Q(total__icontains=search))
        
    context={
        'search_out': search_out,
        }
        
    return render(request,'store/stocksearch.html',context)
        

 
# category
@login_required(login_url='login')
def create_category(request):
    forms = StockCategoryForm()
    if request.method == 'POST':
        forms = StockCategoryForm(request.POST)
        if forms.is_valid():
            category=forms.cleaned_data['category']
            stockCategory.objects.create(
                category=category,
            )
            return redirect('category-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)
    

class CategoryListView(ListView):
    model = stockCategory
    template_name = 'store/category_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = stockCategory.objects.all().order_by('-pk')
        return context


@login_required(login_url='login')   
def update_category(request,pk):
    if request.method == 'POST':
        cp=stockCategory.objects.get(pk=pk)
        form=StockCategoryForm(request.POST, instance=cp)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        cp=stockCategory.objects.get(pk=pk)
        form=StockCategoryForm(instance=cp)
    
    return render(request,'store/updateCategory.html',{'form':form})


    

@login_required(login_url='login')   
def delete_category(request,pk):
    if request.method == 'POST':
        category=stockCategory.objects.get(pk=pk)
        category.delete()
        return redirect('category-list') 
  
    
    


# sub_category
@login_required(login_url='login')
def create_sub_category(request):
    forms = StockSubCategoryForm()
    if request.method == 'POST':
        forms = StockSubCategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('sub-category-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSubCategory.html', context)
    
    

class SubCategoryListView(ListView):
    model = stockSubCategory
    template_name = 'store/subcategory_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_category'] = stockSubCategory.objects.all().order_by('-pk')
        return context

    


@login_required(login_url='login')   
def update_sub_category(request,pk):
    if request.method == 'POST':
        cp=stockSubCategory.objects.get(pk=pk)
        form=StockSubCategoryForm(request.POST, instance=cp)
        if form.is_valid():
            form.save()
            return redirect('sub-category-list')
    else:
        cp=stockSubCategory.objects.get(pk=pk)
        form=StockSubCategoryForm(instance=cp)
    
    return render(request,'store/updateSubCategory.html',{'form':form})

    

@login_required(login_url='login')   
def delete_sub_category(request,pk):

    if request.method == 'POST':
        sub_category=stockSubCategory.objects.get(pk=pk)
        sub_category.delete()
        return redirect('sub-category-list') 
    





# Buyer views
# @login_required(login_url='login')  
# def create_buyer(request):
#     forms = BuyerForm()
#     if request.method == 'POST':
#         forms = BuyerForm(request.POST)
#         if forms.is_valid():
#             name = forms.cleaned_data['name']
#             address = forms.cleaned_data['address']
#             email = forms.cleaned_data['email']
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             retype_password = forms.cleaned_data['retype_password']
#             if password == retype_password:
#                 user = User.objects.create_user(username=username, password=password, email=email, is_buyer=True)
#                 Buyer.objects.create(user=user, name=name, address=address)
#                 return redirect('buyer-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/addbuyer.html', context)

# class BuyerListView(ListView):
#     model = Buyer
#     template_name = 'store/buyer_list.html'
#     context_object_name = 'buyer'
    


