from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

from . import models


class ContextObjectInfoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['OBJECT_NAME'] = self.model.__name__

        QUERYSET_VALUES = {}
        for index, values in enumerate(self.get_queryset().values()):
            QUERYSET_VALUES.update({index: values})
        context['QUERYSET_VALUES'] = QUERYSET_VALUES

        context['OBJECT_VALUES_TO_IGNORE'] = ['abstractmodel_ptr_id']

        return context


class StripeSuccessMessageMixin(SuccessMessageMixin):
    success_message = 'success'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.get_success_message({}))
        return super().delete(request, *args, **kwargs)

    # return a generic success message for certain CRUD view types
    def get_success_message(self, cleaned_data):
        bases = [base.__name__ for base in self.__class__.__bases__]
        object_name = self.model.__name__
        if 'CreateView' in bases:
            self.success_message =\
                f"{object_name} create {self.success_message}"
        elif 'UpdateView' in bases:
            self.success_message =\
                f"{object_name} update {self.success_message}"
        elif 'DeleteView' in bases:
            self.success_message =\
                f"{object_name} delete {self.success_message}"
        return super().get_success_message(cleaned_data)


class StripeCommonViewMixin(ContextObjectInfoMixin, StripeSuccessMessageMixin):
    context_object_name = 'object'

    def dispatch(self, request, *args, **kwargs):
        if self.__class__.__bases__[-1].__name__ == 'CreateView':
            self.fields = ()
        elif self.__class__.__bases__[-1].__name__ == 'UpdateView':
            self.fields = '__all__'
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bases = [base.__name__ for base in self.__class__.__bases__]
        context['action_verb'] = 'create' if 'CreateView' in bases else \
                                 'update' if 'UpdateView' in bases else None
        return context

    def get_success_url(self):
        return reverse(f'stripes:{self.model.__name__.lower()}_list')


# stripe objects
class CustomerViewMixin(StripeCommonViewMixin):
    model = models.Customer
    pk_url_kwarg = 'customer_pk'


class PaymentMethodViewMixin(StripeCommonViewMixin):
    model = models.PaymentMethod
    pk_url_kwarg = 'paymentmethod_pk'
