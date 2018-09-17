# Generated by Django 2.1.1 on 2018-09-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osiso',
            name='stauts',
            field=models.CharField(choices=[('FINISHED', '上传完成'), ('UPLOADING', '上传中'), ('WAITING', '等待上传')], default='UPLOADING', max_length=10),
        ),
        migrations.AlterField(
            model_name='osiso',
            name='md5',
            field=models.CharField(blank=True, default='', max_length=32, unique=True),
        ),
    ]