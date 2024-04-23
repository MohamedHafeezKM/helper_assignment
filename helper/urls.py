from django.contrib import admin
from django.urls import path,include

from helper import views

urlpatterns = [
    path('helpers/add/',views.AddHelperView.as_view(),name='add_helper'),
    path('helpers/all/',views.AllHelpersView.as_view(),name='all_helpers'),
    path('customers/add/',views.AddCustomerView.as_view(),name='add_customer'),
    path('customers/all/',views.AllCustomersView.as_view(),name='all_customers'),
    path('helpers/assign/customers',views.AssigingView.as_view(),name='assign'),
    path('helpers/available/',views.AvailableHelpersView.as_view(),name='available_helpers'),
   
]