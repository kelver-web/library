
from django.urls import path
from checkout.views import (CreateCartItemView, CartItemView, CheckoutView, 
                            OrderListView, OrderDetailView, PagSeguroView, exportar_pedidos_excel)



app_name = 'checkout'

urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', CreateCartItemView.as_view(), name='create_cartitem'),
    path('carrinho/', CartItemView.as_view(), name='cart_item'),
    path('finalizando/', CheckoutView.as_view(), name='checkout'),
    path('finalizando/<int:pk>/pagseguro/', PagSeguroView.as_view(), name='pagseguro_view'),
    path('meus-pedidos/', OrderListView.as_view(), name='order_list'),
    path('meus-pedidos/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('exportar-pedidos-excel/', exportar_pedidos_excel, name='exportar_pedidos_excel'),
]
