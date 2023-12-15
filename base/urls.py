from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home-view'),
    path('menu',menu,name='menu-view'),
    path('customer',CustomerListView.as_view(),name='customer-list-view'), 
    path('customer/<int:pk>',CustomerDetailView.as_view(),name='customer-detail-view'),
    path('customer/add',CustomerCreateView.as_view(),name="customer-create-view"),
    path('customer/update/<int:pk>',CustomerUpdateView.as_view(),name='customer-update-view'),
    path('customer/delete/<int:pk>',CustomerDeleteView.as_view(),name='customer-delete-view'),
    path('product',ProductListView.as_view(),name='product-list-view'), 
    path('product/<int:pk>',ProductDetailView.as_view(),name='product-detail-view'),
    path('product/add',ProductCreateView.as_view(),name="product-create-view"),
    path('product/update/<int:pk>',ProductUpdateView.as_view(),name='product-update-view'),
    path('product/delete/<int:pk>',ProductDeleteView.as_view(),name='product-delete-view'),
]