# Generated by Django 4.1.4 on 2022-12-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_pgn_delete_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pgn',
            options={'ordering': ['name', 'ringnum', 'egg', 'eggnum']},
        ),
        migrations.AlterField(
            model_name='pgn',
            name='childay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pgn',
            name='eggday',
            field=models.DateField(blank=True, null=True),
        ),
    ]