from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


from .models import Product
# Create your views here.

# def homeView(request):
#     template = 'home.html'
#     context = {
#         'products' : Product.objects.all()
#     }
#     return render(request, template, context)

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

def aboutView(request):
    template = 'about.html'
    context = {
    }
    return render(request, template, context)

def contactView(request):
    template = 'contact.html'
    context = {
    }
    return render(request, template, context)



class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'
    success_url = '/'

class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'product'

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'



# 

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "send_email.html", context)