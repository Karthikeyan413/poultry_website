# Generated by Django 4.1.3 on 2023-02-12 14:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0021_alter_chicks_date_alter_chicks_data_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bt_lyr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 137435, tzinfo=datetime.timezone.utc))),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='chicks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 134417, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='chicks_data',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 135435, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='feed_chicks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 136435, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='feed_hen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 138437, tzinfo=datetime.timezone.utc))),
                ('received', models.PositiveIntegerField(default=0)),
                ('meter_reading', models.PositiveIntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
                ('gram_per_bird', models.FloatField(default=0)),
                ('bt_lyr_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eggs.bt_lyr')),
            ],
        ),
        migrations.CreateModel(
            name='eggs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=datetime.datetime(2023, 2, 12, 14, 35, 18, 139436, tzinfo=datetime.timezone.utc), unique=True)),
                ('normal', models.PositiveIntegerField(default=0)),
                ('small', models.PositiveIntegerField(default=0)),
                ('big', models.PositiveIntegerField(default=0)),
                ('broken', models.PositiveIntegerField(default=0)),
                ('damage', models.PositiveIntegerField(default=0)),
                ('day_total', models.PositiveIntegerField(default=0)),
                ('production', models.FloatField(default=0)),
                ('closing', models.PositiveIntegerField(default=0)),
                ('delivery_normal', models.PositiveIntegerField(default=0)),
                ('delivery_big', models.PositiveIntegerField(default=0)),
                ('delivery_small', models.PositiveIntegerField(default=0)),
                ('delivery_broken', models.PositiveIntegerField(default=0)),
                ('to_gate', models.PositiveIntegerField(default=0)),
                ('spoiled', models.PositiveIntegerField(default=0)),
                ('total_birds', models.PositiveIntegerField(default=0)),
                ('sold', models.PositiveIntegerField(default=0)),
                ('mortality', models.PositiveSmallIntegerField(default=0)),
                ('bt_lyr_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eggs.bt_lyr')),
            ],
        ),
        migrations.AddField(
            model_name='bt_lyr',
            name='batch_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eggs.chicks'),
        ),
        migrations.AddField(
            model_name='bt_lyr',
            name='layer_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eggs.layer'),
        ),
        migrations.AlterUniqueTogether(
            name='bt_lyr',
            unique_together={('batch_no', 'layer_no')},
        ),
    ]