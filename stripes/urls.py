from django.urls import path

from . import views

app_name = 'stripes'

urlpatterns = [
  path('', views.stripes_root, name='stripes_root'),

  # customer
  path('customer/',
       views.CustomerListView.as_view(),
       name='customer_list'),
  path('customer/create/',
       views.CustomerCreateView.as_view(),
       name='customer_create'),
  path('customer/<int:customer_pk>/',
       views.CustomerDetailView.as_view(),
       name='customer_detail'),
  path('customer/<int:customer_pk>/update/',
       views.CustomerUpdateView.as_view(),
       name='customer_update'),
  path('customer/<int:customer_pk>/delete/',
       views.CustomerDeleteView.as_view(),
       name='customer_delete'),

  path('customer/payment-methods/link/',
       views.CustomerLinkPaymentMethodView.as_view(),
       name='customer_delete_newest'),
  path('customer/newest/delete/',
       views.CustomerNewestDeleteView.as_view(),
       name='customer_delete_newest'),


  # paymentmethod
  path('paymentmethod/',
       views.PaymentMethodListView.as_view(),
       name='paymentmethod_list'),
  path('paymentmethod/create/',
       views.PaymentMethodCreateView.as_view(),
       name='paymentmethod_create'),
  path('paymentmethod/<int:paymentmethod_pk>/',
       views.PaymentMethodDetailView.as_view(),
       name='paymentmethod_detail'),
  path('paymentmethod/<int:paymentmethod_pk>/update/',
       views.PaymentMethodUpdateView.as_view(),
       name='paymentmethod_update'),
  path('paymentmethod/<int:paymentmethod_pk>/delete/',
       views.PaymentMethodDeleteView.as_view(),
       name='paymentmethod_delete'),

  path('paymentmethod/newest/delete/',
       views.PaymentMethodNewestDeleteView.as_view(),
       name='paymentmethod_delete_newest'),

]
