# Generated by Django 4.1.3 on 2023-01-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0014_alter_eggs_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bt_lyr',
            name='batch_no',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='bt_lyr',
            unique_together={('batch_no', 'layer_no')},
        ),
    ]