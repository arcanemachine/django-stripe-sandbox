import stripe
from django.conf import settings
from django.db import models
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY


class AbstractModel(models.Model):
    def get_absolute_url(self):
        model_name_lowercased = self.__class__.__name__.lower()
        return reverse(f"stripes:{model_name_lowercased}_detail", kwargs={
            f"{model_name_lowercased}_pk": self.pk})

    def __str__(self):
        return str(self.pk)


# class Coupon(models.Model):
#     stripe_coupon = models.JSONField(blank=True, null=True)


class Customer(AbstractModel):
    stripe_customer = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.stripe_customer:
            self.stripe_customer = stripe.Customer.create()
        super().save(*args, **kwargs)


# class Discount(models.Model):
#     stripe_discount = models.JSONField(blank=True, null=True)


# class Dispute(models.Model):
#     stripe_dispute = models.JSONField(blank=True, null=True)


# class Invoice(models.Model):
#     stripe_invoice = models.JSONField(blank=True, null=True)


# class Order(models.Model):
#     stripe_order = models.JSONField(blank=True, null=True)


# class Price(models.Model):
#     stripe_price = models.JSONField(blank=True, null=True)


# class Plan(models.Model):
#     stripe_plan = models.JSONField(blank=True, null=True)


# class Product(models.Model):
#     stripe_product = models.JSONField(blank=True, null=True)


# class PaymentIntent(models.Model):
#     stripe_paymentintent = models.JSONField(blank=True, null=True)


class PaymentMethod(models.Model):
    customer = models.ForeignKey(
        'stripes.Customer', related_name="paymentmethods",
        null=True, on_delete=models.SET_NULL)
    stripe_paymentmethod = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.stripe_paymentmethod:
            self.stripe_paymentmethod = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": "4242424242424242",
                    "exp_month": 12,
                    "exp_year": 2034,
                    "cvc": 123})
        super().save(*args, **kwargs)


# class Quote(models.Model):
#     stripe_quote = models.JSONField(blank=True, null=True)


# class Refund(models.Model):
#     stripe_refund = models.JSONField(blank=True, null=True)


# class Session(models.Model):
#     stripe_session = models.JSONField(blank=True, null=True)


# class SetupIntent(models.Model):
#     stripe_setupintent = models.JSONField(blank=True, null=True)


# class Sku(models.Model):
#     stripe_sku = models.JSONField(blank=True, null=True)


# class Subscription(models.Model):
#     stripe_subscription = models.JSONField(blank=True, null=True)


# class TaxRate(models.Model):
#     stripe_taxrate = models.JSONField(blank=True, null=True)
