from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/products',views.index,name="products" ),
    path('',views.home,name="myhome"),
    path("about/", views.about, name="aboutus"),
   path("contact/", views.contact, name="contact"),
   path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
   path("checkout/", views.checkout, name="checkout"),
   path("productdetail/<int:myid>", views.productView, name="ProductDetails"),


#     path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
