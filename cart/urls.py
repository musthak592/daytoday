from . import views
from django.urls import path
app_name='cart'

urlpatterns=[
    path('',views.cart_detail,name="cart_detail"),
    path('add/<int:product_id>',views.add_cart,name="add_cart"),
    path('remove/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('delete/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('add/<int:product_id>/', views.add_Plus, name='add_Plus'),

]


