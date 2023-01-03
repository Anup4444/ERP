
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

# from users.models import User

class Company(models.Model):
    
    code=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=250,blank=True, null=True)
    address = models.CharField(max_length=220)
    email=models.EmailField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
# staff management
class DropStaff(models.Model):
   
    
    role = models.CharField(max_length=120,primary_key=True)
    # group=models.OneToOneField(Group, on_delete=models.CASCADE)


    def __str__(self):
        return self.role


class staffManagement(models.Model):
    drop = models.ForeignKey(DropStaff, on_delete=models.CASCADE)
    

    code=models.CharField(max_length=100,primary_key=True)
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.code


# Stock
class stockCategory(models.Model):
    
   

    category=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.category

class stockSubCategory(models.Model):
   

    category=models.ForeignKey(stockCategory, on_delete=models.CASCADE)
    sub_category=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.sub_category
    
class Stock(models.Model):
   

    category=models.ForeignKey(stockCategory, on_delete=models.CASCADE, null=True)
    sub_category=models.ForeignKey(stockSubCategory, on_delete=models.CASCADE, null=True)
    code=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    alias_name=models.CharField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    total = models.FloatField(default= 0)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    


# class Buyer(models.Model):
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, unique=True)
#     address = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
    
# class RolesManagement(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=False)
#     group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True, blank=True)
#     role_id = models.CharField(max_length=100, blank=True, null=True, editable=False)
    
#     def __str__(self):
#         return self.group.name
    


