# Generated by Django 2.2.1 on 2019-09-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_projectteamftth_projectteamftts_teammembertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='device',
        ),
    ]