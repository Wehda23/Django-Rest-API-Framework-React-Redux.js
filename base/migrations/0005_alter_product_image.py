# Generated by Django 3.2.9 on 2021-12-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211205_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/default.jpg', null=True, upload_to=''),
        ),
    ]
