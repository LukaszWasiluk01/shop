# Generated by Django 4.0 on 2022-01-07 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('user',), 'verbose_name_plural': 'Addresses'},
        ),
    ]
