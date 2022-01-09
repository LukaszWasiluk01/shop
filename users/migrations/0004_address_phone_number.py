# Generated by Django 4.0 on 2022-01-09 19:21

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_address_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, validators=[users.models.validate_phone_number]),
        ),
    ]