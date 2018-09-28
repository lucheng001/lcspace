# Generated by Django 2.1.1 on 2018-09-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_machineconfig_disk_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmachines',
            name='status',
            field=models.CharField(choices=[('Running', '运行'), ('Creating', '创建中'), ('Failed', '创建失败'), ('Pushed', '待机'), ('Shutdown', '关机')], default='Creating', max_length=10),
        ),
    ]
