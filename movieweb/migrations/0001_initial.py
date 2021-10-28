# Generated by Django 3.2.8 on 2021-10-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('usernmae', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]
