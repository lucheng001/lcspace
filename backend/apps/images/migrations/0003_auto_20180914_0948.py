# Generated by Django 2.1.1 on 2018-09-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180914_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osiso',
            old_name='stauts',
            new_name='status',
        ),
    ]
