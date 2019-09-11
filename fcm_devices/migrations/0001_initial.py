# Generated by Django 2.2.1 on 2019-09-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_id', models.CharField(max_length=50, unique=True, verbose_name='Device ID')),
                ('reg_id', models.CharField(max_length=255, unique=True, verbose_name='Registration ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('owner', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'abstract': False,
            },
        ),
    ]
