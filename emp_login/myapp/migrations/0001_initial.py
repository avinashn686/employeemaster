# Generated by Django 3.1.1 on 2020-09-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=75)),
                ('phonenumber', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
