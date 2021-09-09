from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView

from django_stripe_sandbox.mixins import ContextObjectInfoMixin
from .models import Customer


class MySuccessMessageMixin(SuccessMessageMixin):
    success_message = 'success'

    def delete(self, request, *args, **kwargs):
        messages.success(
            request, self.success_message,
            extra_tags='success')
        return super().delete(request, *args, **kwargs)


class MyViewMixin:
    context_object_name = 'object'


def stripes_root(request):
    return render(request, 'stripes/stripes_root.html')


# customer
class CustomerViewMixin:
    model = Customer
    context_object_name = 'object'
    pk_url_kwarg = 'customer_pk'
    success_url = reverse_lazy('stripes:customer_list')


class CustomerListView(ContextObjectInfoMixin, MyViewMixin, CustomerViewMixin,
                       MySuccessMessageMixin, ListView):
    pass


class CustomerCreateView(ContextObjectInfoMixin, MyViewMixin,
                         CustomerViewMixin, MySuccessMessageMixin, CreateView):
    fields = ()


class CustomerDetailView(ContextObjectInfoMixin, MyViewMixin,
                         CustomerViewMixin, MySuccessMessageMixin, DetailView):
    pass


class CustomerUpdateView(ContextObjectInfoMixin, MyViewMixin,
                         CustomerViewMixin, MySuccessMessageMixin, UpdateView):
    fields = '__all__'


class CustomerDeleteView(ContextObjectInfoMixin, MyViewMixin,
                         CustomerViewMixin, MySuccessMessageMixin, DeleteView):
    pass
