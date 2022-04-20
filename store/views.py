from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from .models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm, SearchForm



# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "store/products/list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        base_url = self.request.get_full_path()
        if self.request.GET:
            page = self.request.GET.get('page')
            if page:
                number = len(page)
                number *= -1
                base_url = base_url[:number]
            else:
                base_url += "&page="
        else:
            base_url += "?page="

        context['pagination_url'] = base_url
        context['form'] = SearchForm(self.request.GET)

        name = self.request.GET.get('name')
        if name:
            context['name'] = name
        return context

    def get_queryset(self):
        selectors = {
            'name__icontains' : self.request.GET.get('name'),
            'price__gte' : self.request.GET.get('price_from'),
            'price__lte' : self.request.GET.get('price_to'),
            'category__slug': self.kwargs.get("slug")
        }
        selectors = {k: v for k, v in selectors.items() if v}
        selectors["available"] = True

        queryset = Product.objects.filter(**selectors)
        return queryset

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm(product.quantity_left)
    return render(request,
                  'store/products/detail.html',
                  {'product':product,
                  'cart_product_form':cart_product_form,})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(product.quantity_left,request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('store:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('store:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        product = get_object_or_404(Product, id=item['product'].id)
        item['update_quantity_form'] = CartAddProductForm(product.quantity_left,initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'store/products/cart.html', {'cart': cart})