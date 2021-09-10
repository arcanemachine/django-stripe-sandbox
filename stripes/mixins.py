from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Customer


# mixins
class StripeSuccessMessageMixin(SuccessMessageMixin):
    success_message = 'success'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


class CommonViewMixin:
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bases = [base.__name__ for base in self.__class__.__bases__]
        context['action_verb'] = 'create' if 'CreateView' in bases else \
                                 'update' if 'UpdateView' in bases else None
        return context


class CustomerViewMixin:
    model = Customer
    pk_url_kwarg = 'customer_pk'
    success_url = reverse_lazy('stripes:customer_list')
