# Generated by Django 5.1.1 on 2024-10-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "product",
            "0002_product_manufactured_at_alter_product_creation_date_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]
