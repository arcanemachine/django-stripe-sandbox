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
  path('customer/newest/delete/',
       views.CustomerNewestDeleteView.as_view(),
       name='customer_delete_newest'),
  path('customer/<int:customer_pk>/delete/',
       views.CustomerDeleteView.as_view(),
       name='customer_delete'),
]
