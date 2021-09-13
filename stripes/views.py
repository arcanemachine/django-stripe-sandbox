from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView

from .mixins import CommonViewMixin, CustomerViewMixin, \
    PaymentMethodViewMixin, StripeSuccessMessageMixin
from django_stripe_sandbox.mixins import ContextObjectInfoMixin


# stripes_root
def stripes_root(request):
    return render(request, 'stripes/stripes_root.html')


# customer
class CustomerListView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, ListView):
    pass


class CustomerDetailView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DetailView):
    pass


class CustomerCreateView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, CreateView):
    pass


class CustomerUpdateView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, UpdateView):
    pass


class CustomerDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    pass


class CustomerNewestDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    def get_object(self):
        return self.model.objects.last()


# paymentmethod
class PaymentMethodListView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, ListView):
    pass


class PaymentMethodDetailView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, DetailView):
    pass


class PaymentMethodCreateView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, CreateView):
    pass


class PaymentMethodUpdateView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, UpdateView):
    pass


class PaymentMethodDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    pass


class PaymentMethodNewestDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, PaymentMethodViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    def get_object(self):
        return self.model.objects.last()


