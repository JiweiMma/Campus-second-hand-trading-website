# Generated by Django 3.0.2 on 2020-01-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TransApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sellbag_num',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shoppingcart_num',
        ),
    ]
