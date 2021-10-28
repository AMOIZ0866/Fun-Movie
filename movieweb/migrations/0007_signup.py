# Generated by Django 3.2.8 on 2021-10-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movieweb', '0006_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('type', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField()),
                ('creation_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]
