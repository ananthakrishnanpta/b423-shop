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

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search_bar'] = True
        return context

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



def searchView(request):
    query = request.GET.get('q')
    result_products = Product.objects.filter(title__icontains = query)
    context = {
        'query' : query,
        'products' : result_products
    }
    template = 'search_results.html'

    return render(request, template, context)

