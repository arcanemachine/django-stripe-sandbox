import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, FormView,\
    ListView, UpdateView

from . import forms
from .mixins import CustomerViewMixin, PaymentMethodViewMixin
from .models import Customer, PaymentMethod

stripe.api_key = settings.STRIPE_SECRET_KEY


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


# customer - custom views - update
class CustomerAttachPaymentMethodView(FormView):
    template_name = 'stripes/customer_form.html'
    form_class = forms.CustomerAttachPaymentMethodForm

    def form_valid(self, form):
        try:
            # link the PaymentMethod to the stripe Customer object
            customer = get_object_or_404(
                Customer, pk=form.cleaned_data['customer'])
            paymentmethod = get_object_or_404(
                PaymentMethod, pk=form.cleaned_data['paymentmethod'])
            paymentmethod.stripe_paymentmethod = stripe.PaymentMethod.attach(
                paymentmethod.stripe_paymentmethod['id'],
                customer=customer.stripe_customer['id'])

            # add the PaymentMethod to the Customer's PaymentMethods
            paymentmethod.customer = customer

            # save the updated PaymentMethod data
            paymentmethod.save()


            messages.success(
                self.request,
                f"PaymentMethod #{paymentmethod.pk} attached to "
                f"Customer #{customer.pk}")

        except Exception as e:
            # show exception as status message
            messages.error(self.request, e)
            messages.error(
                self.request,
                f"PaymentMethod #{paymentmethod.pk} could not be attached to "
                f"Customer #{customer.pk}")
        return redirect(customer)


# customer - custom views - delete
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
