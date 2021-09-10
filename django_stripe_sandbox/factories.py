import factory

from stripes.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    """
    Usage:
        - Create object and save: e.g. customer = CustomerFactorr()
        - Build object but don't save: e.g. customer = CustomerFactory.build()
    """
    class Meta:
        model = Customer
