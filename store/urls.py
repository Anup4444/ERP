from django.urls import path


from .views import (
    
    # create_buyer,
    create_company,
    update_company,
    delete_company,
    create_staff,
    create_drop_staff,
    update_staff,
    delete_staff,
    create_stock,
    update_stock,
    delete_stock,
    stock_search,
    create_category,
    update_category,
    delete_category,
    create_sub_category,
    update_sub_category,
    delete_sub_category,
    # add_staff_group,
    
  
    
    # BuyerListView,
    CompanyListView,
    StaffListView,
    StockListView,
    CategoryListView,
    SubCategoryListView,
)

urlpatterns = [
    # company
    path('create-company/', create_company, name='create-company'),
    
    path('update-company/<int:pk>',update_company,name="update-company"),
    path('delete-company/<int:pk>',delete_company,name="delete-company"),
    
    #  staff
    path('create-staff/', create_staff, name='create-staff'),
    path('create-drop-staff/',create_drop_staff,name='create-drop-staff'),
    
    path('update-staff/<int:pk>',update_staff,name="update-staff"),
    path('delete-staff/<int:pk>',delete_staff,name="delete-staff"),
    
    #stock category
    path('create-category/',create_category,name='create-category'),
    path('update-category/<int:pk>', update_category,name="update-category"),
    path('delete-category/<int:pk>',delete_category,name="delete-category"),
    
    # stock sub category
    path('create-sub-category/',create_sub_category,name='create-sub-category'),
    path('update-sub-category/<int:pk>',update_sub_category,name="update-sub-category"),
    path('delete-sub-category/<int:pk>',delete_sub_category,name="delete-sub-category"),
    
    
  
    
 
    
    
    
#   stock
    path('create-stock/',create_stock,name='create-stock'),
    path('update-stock/<int:pk>',update_stock,name="update-stock"),
    path('delete-stock/<int:pk>',delete_stock,name="delete-stock"),
    path('stock-search/',stock_search,name="stock-search"),
     
# buyer
    # path('create-buyer/', create_buyer, name='create-buyer'),



    path('stock-list/',StockListView.as_view(),name='stock-list'),
    path('category-list/',CategoryListView.as_view(),name='category-list'),
    path('sub-category-list/',SubCategoryListView.as_view(),name='sub-category-list'),
    path('staff-list/', StaffListView.as_view(), name='staff-list'),
    path('company-list/', CompanyListView.as_view(), name='company-list'),
    
    
    # path('group/',add_staff_group,name='group'),
    # buyer list
    # path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    
]