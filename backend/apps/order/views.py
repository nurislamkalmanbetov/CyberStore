from itertools import product
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import CreateView, ListView
# Create your views here.
from backend.apps.order.forms import OrderForm
from backend.apps.order.models import Order, OrderItem
from backend.apps.cart.cart import Cart


class OrderCreateView(CreateView, View):
    form_class = OrderForm
    template_name = "order_create.html"
    success_url = reverse_lazy("main_page")


    def form_valid(self, form):
        if self.request.user.is_authenticated:
            order = form.save(commit=False)

            order.user = self.request.user
            cart = Cart(self.request)

            if cart.coupon:
                order.coupon = cart.coupon
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    product=item['product'],
                    order=order,
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return super().form_valid(form)
        else:
            return reverse_lazy('login.html')

# оформление моих заказов
class MyOrders(ListView):
    model = Order
    template_name = 'my_order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyOrders, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user.id)
        return context