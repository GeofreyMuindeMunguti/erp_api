# Generated by Django 2.2.1 on 2019-08-24 19:11

from django.db import migrations, models
import erp_core.fileshandler.filemixin


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0018_auto_20190824_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteclearingdate',
            name='no_of_casuals_atsite',
        ),
        migrations.AlterField(
            model_name='siteclearingdate',
            name='casuals_list',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDir('files/Casuals/DateSetSiteClearing/%Y/%m/%d/')),
        ),
        migrations.AlterField(
            model_name='siteclearingimage',
            name='setting_site_clearing_image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDir('images/CivilWorksTeam/dailysiteclearing/%Y/%m/%d/')),
        ),
    ]
