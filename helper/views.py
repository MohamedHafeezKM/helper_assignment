from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from django.db.models import Count

from helper.forms import HelperForm,CustomerForm
from helper.models import Helper,Customer
# Create your views here.


class AddHelperView(View):
    def get(self,request,*args,**kwargs):
        form=HelperForm()
        return render(request,'add_helper.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=HelperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Added')
            return redirect('all_helpers')
        else:
            messages.error(request,'Failed due to errors')
            return render(request,'add_helper.html',{'form':form})
        

class AllHelpersView(View):
    def get(self,request,*args,**kwargs):
        qs=Helper.objects.all()
        return render(request,'all_helpers.html',{'all_helpers':qs})
    

class AddCustomerView(View):
    def get(self,request,*args,**kwargs):
        form=CustomerForm()
        return render(request,'add_customer.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Added')
            return redirect('all_customers')
        else:
            messages.error(request,'Failed due to errors')
            return render(request,'add_customer.html',{'form':form})
        


class AllCustomersView(View):
    def get(self,request,*args,**kwargs):
        qs=Customer.objects.all()
        return render(request,'all_customers.html',{'all_customers':qs})
    

class AssigingView(View):
    def get(self,request,*args,**kwargs):
        qs=Helper.objects.filter(customer=None)
        available_customers=Customer.objects.filter(helper=None)
        return render(request,'assign.html',{'all_helpers':qs,'available_customers':available_customers})
    
    def post(self,request,*args,**kwargs):
        customer=request.POST.get('assign')
        helper=request.POST.get('helper')
        qs=Helper.objects.filter(id=helper)
        qs.update(customer=customer)
        messages.success(request,'A Helper have to be assigned to a custome')
        return redirect('assign')
    


class AvailableHelpersView(View):
    def get(self,request,*args,**kwargs):
        qs=Helper.objects.filter(customer=None)
        return render(request,'available_helpers.html',{'all_helpers':qs})

    
