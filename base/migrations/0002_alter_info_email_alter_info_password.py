# Generated by Django 4.1.4 on 2022-12-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='password',
            field=models.CharField(max_length=15),
        ),
    ]
