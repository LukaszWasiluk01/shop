from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category

# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "store/products/list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)

        selectors = {
            'title' : self.request.GET.get('title'),
            'category' : self.request.GET.get('category'),
            'min_price' : self.request.GET.get('min_price'),
            'max_price' : self.request.GET.get('max_price'),
        }
        
        if selectors['title']:
            queryset = queryset.filter(name__icontains=selectors['title'])
        if selectors['category'] and selectors['category'] != "Categories":
            queryset = queryset.filter(category__name=selectors['category'])
        if selectors['min_price'] and selectors['max_price']:
            queryset = queryset.filter(price__range=[selectors['min_price'],selectors['max_price']])
        else:
            if selectors['min_price']:
                queryset = queryset.filter(price__gte=selectors['min_price'])
            elif selectors['max_price']:
                queryset = queryset.filter(price__lte=selectors['max_price'])
        return queryset

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'store/products/detail.html',
                  {'product':product})