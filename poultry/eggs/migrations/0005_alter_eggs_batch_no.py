# Generated by Django 4.1.2 on 2022-11-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0004_bt_lyr_eggs_batch_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='batch_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eggs.bt_lyr'),
        ),
    ]
