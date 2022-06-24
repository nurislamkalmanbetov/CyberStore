from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('about/', about_page, name="about"),
    path('mac/', mac_detail, name='mac_detail'),
    path('watch/', watch_detail, name='watch_detail'),
    path('iphone/', iphone_detail, name='iphone_detail'),
    path('contact/', contact_page, name="contact"),
    path('list/product/', ProductListView.as_view(), name='product_list'),
    path('list/category/<slug:slug>/', ProductListView.as_view(), name="category_products"),
    path('detail/product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('search/', ProductSearchView.as_view(), name="search"),
    path('favorite/add/<str:pk>/', favorite_product, name='favorite'),
    path('list/favorites/', favorites_list, name='favorites_product'),
    path('favorite/delete/<str:pk>/', delete_product, name='del_favorite')
]

# 'list/category/avtotovary/'
#'list/category/obuv/jenskaya/'