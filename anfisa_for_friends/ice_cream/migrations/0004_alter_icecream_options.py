# Generated by Django 3.2.16 on 2023-08-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_auto_20230814_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
    ]
