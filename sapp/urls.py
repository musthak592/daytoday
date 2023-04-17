from sapp import views
from django.urls import path
app_name='sapp'

urlpatterns=[
    path('',views.shop,name="shop"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('clients/', views.clients, name="clients"),
    path('<slug:c_slug>', views.clients, name="products_by_category"),

    path('<slug:c_slug>/<slug:product_slug>/', views.ProCatDetail, name='ProCatDetail')

]