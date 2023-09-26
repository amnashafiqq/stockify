from django.contrib import admin
from django.urls import path
from store.views.checkout import CheckOut
from store.middlewares.auth import auth_middleware
from .import views


urlpatterns = [

  # path('check-out', CheckOut.as_view(), name='checkout'),
  path('product-page', views.product_page, name='product-page'),
  path('payment-successful',views.payment_successful,name='payment-successful'),
  path('payment-cancelled',views.payment_cancelled,name='payment_cancelled'),
  path('stripe-webhook',views.stripe_webhook,name='stripe_webhook'),

] 