import factory

from stripes import models as stripes_models


class CustomerFactory(factory.django.DjangoModelFactory):
    """
    Usage:
        - Create object and save: e.g. customer = CustomerFactorr()
        - Build object but don't save: e.g. customer = CustomerFactory.build()
    """
    class Meta:
        model = stripes_models.Customer


class PaymentMethodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = stripes_models.PaymentMethod
