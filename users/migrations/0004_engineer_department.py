# Generated by Django 2.2.1 on 2019-05-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190524_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
