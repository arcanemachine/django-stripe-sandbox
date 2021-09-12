from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView

from django_stripe_sandbox.mixins import ContextObjectInfoMixin
from .mixins import CommonViewMixin, CustomerViewMixin, \
    StripeSuccessMessageMixin
from .models import Customer


# stripes_root
def stripes_root(request):
    return render(request, 'stripes/stripes_root.html')


# customer
class CustomerListView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, ListView):
    pass


class CustomerCreateView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, CreateView):
    fields = ()


class CustomerDetailView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DetailView):
    def get_queryset(self):
        return Customer.objects.filter(id=self.kwargs['customer_pk'])


class CustomerUpdateView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, UpdateView):
    fields = '__all__'


class CustomerDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    pass


class CustomerNewestDeleteView(
        ContextObjectInfoMixin, CommonViewMixin, CustomerViewMixin,
        StripeSuccessMessageMixin, DeleteView):
    def get_object(self):
        return Customer.objects.last()
