# Generated by Django 2.2.28 on 2023-04-27 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230427_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 22, 42, 50, 749433), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 22, 42, 50, 750384), verbose_name='Дата комментария'),
        ),
    ]