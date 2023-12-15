from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Customer,Product
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import SearchForm, ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request): 
    return render(request,'base/home.html')
def menu(request): 
    return render(request,'base/menu.html')


########################CUSTOMER VIEWS#####################################3

class CustomerListView(ListView):
    model = Customer 
    context_object_name = "customer_list"

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name= "customer_detail"

class CustomerCreateView(CreateView): 
    model = Customer 
    fields= ['name','brands','status']
    template_name = 'base/customer_create_form.html'
    success_url=reverse_lazy('customer-list-view')

class CustomerUpdateView(UpdateView): 
    model = Customer
    fields = ["name","brands","status"]
    template_name = 'base/customer_update_form.html'

class CustomerDeleteView(DeleteView): 
    model = Customer 

    def delete(self,*args,**kwargs): 
        customer = self.get_object()
        customer.delete()
        return JsonResponse({
            'status':'success'
        })


####################PRODUCT VIEWS#####################################33

class ProductListView(ListView): 
    model = Product 
    template_name = "base/product_list.html"
    context_object_name = "product_list"
    paginate_by = 10 

    def get_queryset(self): 
        searchform = SearchForm(self.request.GET)
        query = searchform['query'].value() if searchform.is_valid else ''
        searchfilter = (
            Q(name__icontains=query) | Q(legal_name__icontains=query) | Q(brand__icontains=query) | Q(customer__name__icontains=query)
        )
        if query : 
            return Product.objects.filter(searchfilter)
        return Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        start_index = page.number*self.paginate_by - (self.paginate_by-1)
        end_index = page.number*self.paginate_by + 1
        global_index = [i for i in range(start_index,end_index)]
        context["query"] = self.request.GET.get('query','')
        context["searchform"] = SearchForm(self.request.GET)
        context["index"] = global_index
        return context 
 

class ProductDetailView(DetailView): 
    model = Product 
    context_object_name = "product_detail"
    

class ProductCreateView(CreateView): 
    model = Product 
    # fields=['name','legal_name','brand','customer','volume','type','domestic_distribution','export_distribution','remark']
    template_name = "base/product_create_form.html"
    form_class = ProductForm
    success_url = reverse_lazy('product-list-view')

class ProductUpdateView(UpdateView): 
    model = Product
    # fields=['name','legal_name','brand','customer','volume','type','domestic_distribution','export_distribution','remark']
    template_name = 'base/product_update_form.html'
    form_class=ProductForm

class ProductDeleteView(DeleteView): 
    model = Product

    def delete(self,*args,**kwargs): 
        product = self.get_object()
        product.delete()
        return JsonResponse({
            'status':'success'
        })





