from django.contrib import admin
from .models import Company

from .models import (
    
    # Buyer,
    stockCategory,
    stockSubCategory,
    Stock,
    
    
    
    
    
    
    staffManagement,
    DropStaff,
)


# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'name', 'address', 'created_date']

# admin.site.register(Buyer, BuyerAdmin)

admin.site.register(Stock)

admin.site.register(stockCategory)

admin.site.register(stockSubCategory)
admin.site.register(Company)
admin.site.register(staffManagement)
admin.site.register(DropStaff)