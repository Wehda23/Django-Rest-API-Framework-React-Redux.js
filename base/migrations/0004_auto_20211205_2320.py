# Generated by Django 3.2.9 on 2021-12-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='orders',
            new_name='order',
        ),
        migrations.AlterField(
            model_name='product',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]