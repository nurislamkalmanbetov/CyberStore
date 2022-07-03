from re import template
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

import json
# Create your views here.
from .models import Category , Product





class MainPage(TemplateView):
    template_name = "main_page.html"


def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")

def mac_detail(request):
    return render(request, "mac_detail.html")

def watch_detail(request):
    return render(request, "watch_detail.html")

def iphone_detail(request):
    return render(request, "iphone_detail.html")



class ProductListView(ListView, View):
    template_name = "product_list.html"
    model = Product
    # context_object_name = 'products'
    paginate_by = 16
    #стандартное имя списка продуктов в шаблоне
    # для ListView - object_list

    def get_queryset(self, **kwargs):
        search_query = self.request.GET.get('search', '')
        category_slug = self.kwargs.get("slug")
        print(category_slug)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(is_active=True, category=category)
            return queryset
        return self.model.objects.filter(is_active=True)

        # elif search_query:
        #     if search_query:
        #         queryset = self.model.objects.filter(name__icontains=self.request.GET.get('search', ''),
        #                                              is_active=True
        #                                              )
        #         return queryset
        #     else:
        #         return 'asd'



class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product" # стандартный object


class ProductSearchView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10

    @property
    def get_queryset(self):
        search_text = self.request.GET.get("query")
        if search_text is None:
            return self.model.objects.filter(is_active=True)
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            |Q(description__icontains=search_text)
        )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get("query")
        return context



def favorites_list(request):
    user = request.user
    favorite_products = user.favorite.all()
    return render(request, 'favorite_list.html', context={'favorite_products': favorite_products})


def favorite_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.favorite.filter(id=request.user.id).exists():
        product.favorite.remove(request.user)
    else:
        product.favorite.add(request.user)
    return redirect('product_list')


def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.favorite.filter(id=request.user.id).exists():
        product.favorite.remove(request.user)
    return redirect('favorites_product')

