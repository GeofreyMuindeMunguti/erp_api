# Generated by Django 2.2.1 on 2019-08-25 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0024_auto_20190825_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btssite',
            old_name='bts_project_name',
            new_name='project_name',
        ),
    ]
