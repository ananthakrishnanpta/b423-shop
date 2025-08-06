from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HomeView.as_view() , name = 'homepage'),
    path('about', views.aboutView, name = 'aboutpage'),
    path('contact', views.contactView, name = 'contactpage'),
    path('products/add', views.AddProduct.as_view(), name = 'addproduct'),
    path('product/<int:pk>', views.ProductDetails.as_view(), name= 'prod_details'),
    path('product/update/<int:pk>', views.UpdateProduct.as_view(), name = 'updateproduct'),
    path('product/delete/<int:pk>', views.DeleteProduct.as_view(), name = 'deleteproduct'),
    
]