# Generated by Django 3.2.7 on 2021-09-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripes', '0002_alter_customer_stripe_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_paymentmethod', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
