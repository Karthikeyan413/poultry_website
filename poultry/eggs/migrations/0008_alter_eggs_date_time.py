# Generated by Django 4.1.2 on 2022-11-15 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0007_eggs_mortality_eggs_sold_eggs_total_birds_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='date_time',
            field=models.DateField(default=datetime.date(2022, 11, 15), editable=False, unique=True),
        ),
    ]
