# Generated by Django 4.1.4 on 2023-01-12 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_address_date_added_alter_orderitem_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='date_added',
        ),
    ]
