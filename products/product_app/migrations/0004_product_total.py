# Generated by Django 3.2.5 on 2021-07-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_auto_20210707_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]