from django import forms

from .models import Customer, PaymentMethod


class CustomerLinkPaymentMethodForm(forms.Form):
    customer = forms.ChoiceField()
    paymentmethod = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customer
        self.fields['customer'].choices =\
            [(customer.pk, f"Customer #{customer.pk}")
                for customer in Customer.objects.all()]

        # PaymentMethod
        self.fields['paymentmethod'].choices =\
            [(paymentmethod.pk, f"PaymentMethod #{paymentmethod.pk}")
                for paymentmethod in PaymentMethod.objects.all()]
