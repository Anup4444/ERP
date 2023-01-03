from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from store.models import Company,staffManagement,Stock
from store.forms import CompanyForm




@login_required(login_url='login')
def dashboard(request):
  

    # total_buyer = Buyer.objects.count()

    total_staff=staffManagement.objects.count()
    total_company=Company.objects.count()
    total_stock=Stock.objects.count()

    context = {
   
  
        # 'buyer': total_buyer,

        'company':total_company,
        'staff':total_staff,
        'stock':total_stock,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def register_company(request):
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
            return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'registerCompany.html', context)