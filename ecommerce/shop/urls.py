"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from shop.views import ProductDetailView

app_name='shop'


urlpatterns = [
    path('',views.CategoryListView.as_view(),name="category"),
    path('product/<int:i>/',views.ProductListView.as_view(), name="product"),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
    path('register/',views.Register.as_view(),name="register"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',views.Logout.as_view(),name="logout"),
    path('allproducts',views.AllProducts.as_view(),name="allproducts"),
    path('addproduct',views.AddProduct.as_view(),name="addproducts"),
    path('addcategory',views.AddCategory.as_view(),name="addcategory"),
    path('addstock/<int:pk>',views.AddStock.as_view(),name="addstock")

]





