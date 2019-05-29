# Generated by Django 2.2.1 on 2019-05-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0002_auto_20190529_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installationteam',
            name='final_acceptance_cert',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='final_acceptance_cert_comment',
        ),
        migrations.AddField(
            model_name='project',
            name='final_acceptance_cert',
            field=models.FileField(blank=True, null=True, upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='project',
            name='final_acceptance_cert_comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
