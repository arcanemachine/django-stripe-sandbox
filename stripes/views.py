from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView

from .mixins import CustomerViewMixin, PaymentMethodViewMixin


# stripes_root
def stripes_root(request):
    return render(request, 'stripes/stripes_root.html')


# customer
class CustomerListView(CustomerViewMixin, ListView):
    pass


class CustomerCreateView(CustomerViewMixin, CreateView):
    pass


class CustomerDetailView(CustomerViewMixin, DetailView):
    pass


class CustomerUpdateView(CustomerViewMixin, UpdateView):
    pass


class CustomerDeleteView(CustomerViewMixin, DeleteView):
    pass


class CustomerNewestDeleteView(CustomerViewMixin, DeleteView):
    def get_object(self):
        return self.model.objects.last()


# paymentmethod
class PaymentMethodListView(PaymentMethodViewMixin, ListView):
    pass


class PaymentMethodCreateView(PaymentMethodViewMixin, CreateView):
    pass


class PaymentMethodDetailView(PaymentMethodViewMixin, DetailView):
    pass


class PaymentMethodUpdateView(PaymentMethodViewMixin, UpdateView):
    pass


class PaymentMethodDeleteView(PaymentMethodViewMixin, DeleteView):
    pass


class PaymentMethodNewestDeleteView(PaymentMethodViewMixin, DeleteView):
    def get_object(self):
        return self.model.objects.last()
