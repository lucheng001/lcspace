# Generated by Django 2.1.1 on 2018-09-25 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmachines',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machineconfig',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
