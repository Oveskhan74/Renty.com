# Generated by Django 5.0.1 on 2024-02-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renty', '0015_alter_property_details_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
