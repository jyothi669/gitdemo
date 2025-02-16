from django.contrib.auth import logout



from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from shop.forms import RegisterForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from shop.models import Category,Product

class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'  # Name of the template to render categories
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = 'product.html'  # Name of the template to render products
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('i')  # ✅ Get category ID from the URL
        category = get_object_or_404(Category, id=category_id)  # ✅ Ensure category exists
        products = Product.objects.filter(category=category)  # ✅ Fetch products under this category

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('i')
        context['category'] = get_object_or_404(Category, id=category_id)  # ✅ Pass category to the template
        return context




class ProductDetailView(DetailView):
        model = Product
        template_name = 'product_detail.html'  # The template to render
        context_object_name = 'product'



class AllProducts(ListView):
    model=Product
    template_name = 'allproducts.html'
    context_object_name = 'allproducts'




class Register(CreateView):
    template_name = 'register.html'
    model = User
    # fields = ['username','password','email','first_name','last_name']
    form_class = RegisterForm
    success_url = reverse_lazy('shop:login')

    def form_valid(self, form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        cp=form.cleaned_data['confirm_password']
        e = form.cleaned_data['email']
        f = form.cleaned_data['first_name']
        l = form.cleaned_data['last_name']
        if p==cp:
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:login')
        else:
            messages.error(self.request,"Passwords doesn't match")
            return redirect('shop:register')


class Login(LoginView):
    template_name="login.html"

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:category')



class AddProduct(CreateView):
    model = Product
    fields=['name','image','desc','price','stock','category']
    template_name = 'addproducts.html'  # Name of the template to render categories
    success_url=reverse_lazy('shop:category')


class AddCategory(CreateView):
    model = Category
    fields=['name','desc','image']
    template_name = 'addcategory.html'  # Name of the template to render categories
    success_url = reverse_lazy('shop:category')


class AddStock(UpdateView):
    model = Product
    fields=['stock']
    template_name = 'addstock.html' # Name of the template to render categories
    success_url = reverse_lazy('shop:product_detail')


























