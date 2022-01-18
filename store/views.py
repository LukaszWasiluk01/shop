from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from .models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


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
                print('base_url: ', base_url)
            else:
                base_url += "&page="
        else:
            base_url += "?page="

        context['pagination_url'] = base_url
        return context

    def get_queryset(self):
        selectors = {
            'title' : self.request.GET.get('title'),
            'category' : self.request.GET.get('category'),
            'min_price' : self.request.GET.get('min_price'),
            'max_price' : self.request.GET.get('max_price'),
        }

        queryset = Product.objects.filter(available=True)
        
        if selectors['category']:
            queryset = queryset.filter(category__name=selectors['category'])
            self.request.session['category'] = selectors['category']
        else:
            self.request.session['category'] = ""
        if selectors['min_price'] and selectors['max_price']:
            queryset = queryset.filter(price__range=[selectors['min_price'],selectors['max_price']])
            self.request.session['min_price'] = selectors['min_price']
            self.request.session['max_price'] = selectors['max_price']
        else:
            if selectors['min_price']:
                queryset = queryset.filter(price__gte=selectors['min_price'])
                self.request.session['min_price'] = selectors['min_price']
            else:
                self.request.session['min_price'] = ""
            if selectors['max_price']:
                queryset = queryset.filter(price__lte=selectors['max_price'])
                self.request.session['max_price'] = selectors['max_price']
            else:
                self.request.session['max_price'] = ""
        if selectors['title']:
            queryset = queryset.filter(name__icontains=selectors['title'])
            self.request.session['title'] = selectors['title']
        else:
            self.request.session['title'] = ""
        
        self.request.session.modified = True
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