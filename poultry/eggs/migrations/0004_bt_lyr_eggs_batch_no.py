# Generated by Django 4.1.2 on 2022-11-06 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0003_alter_eggs_big_alter_eggs_broken_alter_eggs_closing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bt_lyr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.PositiveSmallIntegerField(unique=True)),
                ('layer_no', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='eggs',
            name='batch_no',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='eggs.bt_lyr'),
        ),
    ]
