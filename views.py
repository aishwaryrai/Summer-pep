from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'stock_quantity']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'stock_quantity']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')