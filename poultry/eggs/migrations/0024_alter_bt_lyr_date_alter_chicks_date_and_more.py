# Generated by Django 4.1.3 on 2023-03-04 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0023_alter_bt_lyr_date_alter_chicks_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bt_lyr',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 980008, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='chicks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 978010, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='chicks_data',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 979009, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='eggs',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 981008, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='feed_chicks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 980008, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='feed_hen',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 8, 10, 43, 981008, tzinfo=datetime.timezone.utc)),
        ),
    ]