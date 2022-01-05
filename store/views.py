from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category

# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "store/products/list.html"
    queryset = Product.objects.all()
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context