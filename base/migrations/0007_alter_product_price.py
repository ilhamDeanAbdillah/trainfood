# Generated by Django 4.1.4 on 2022-12-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_order_date_orderd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=1000, null=True),
        ),
    ]
