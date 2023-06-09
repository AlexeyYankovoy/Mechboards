# Generated by Django 2.2.28 on 2023-04-27 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230427_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 22, 2, 32, 100312), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 22, 2, 32, 101349), verbose_name='Дата комментария'),
        ),
    ]
