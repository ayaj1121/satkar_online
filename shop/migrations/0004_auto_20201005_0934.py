# Generated by Django 3.1 on 2020-10-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_customer_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cart',
            field=models.JSONField(blank=True, default={'cart': {}, 'cartitemprice': {}, 'catitem': {}}, null=True),
        ),
    ]
