# Generated by Django 5.0.1 on 2024-02-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renty', '0014_rename_ward_no_property_details_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
