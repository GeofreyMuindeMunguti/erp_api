# Generated by Django 2.2.1 on 2019-05-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installationteam',
            name='integration_parameter',
            field=models.BooleanField(default=False),
        ),
    ]
