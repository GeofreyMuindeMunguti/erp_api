# Generated by Django 2.2.1 on 2019-06-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0002_installationteam_as_built'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialteam',
            name='approved_quote_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commercialteam',
            name='approved_quote_file',
            field=models.FileField(blank=True, null=True, upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/'),
        ),
    ]