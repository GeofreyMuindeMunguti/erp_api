# Generated by Django 2.2.1 on 2019-09-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='device',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]