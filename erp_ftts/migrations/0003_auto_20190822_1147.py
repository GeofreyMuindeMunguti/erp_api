# Generated by Django 2.2.1 on 2019-08-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_ftts', '0002_auto_20190822_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilworkproduction',
            name='site_name',
        ),
        migrations.AddField(
            model_name='sitetrenching',
            name='civilworkproduction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchingcivil', to='erp_ftts.CivilWorkProduction'),
        ),
    ]
