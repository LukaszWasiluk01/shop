# Generated by Django 4.0 on 2022-01-07 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('street', models.CharField(blank=True, max_length=50)),
                ('house_number', models.CharField(blank=True, max_length=5)),
                ('zip_code', models.CharField(blank=True, max_length=6)),
                ('city', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
