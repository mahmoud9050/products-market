# Generated by Django 3.2.5 on 2021-07-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Not Available', 'Not Available'), ('Sold', 'Sold')], max_length=100, null=True),
        ),
    ]
