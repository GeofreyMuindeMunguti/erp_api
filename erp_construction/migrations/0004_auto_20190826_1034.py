# Generated by Django 2.2.1 on 2019-08-26 07:34

from django.db import migrations, models
import django.db.models.deletion
import erp_core.fileshandler.filemixin


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('erp_construction', '0003_auto_20190826_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='gateinstallation_image_1',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='gateinstallation_image_2',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='gateinstallation_image_3',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='no_of_casuals_atsite',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='gateinstallationimage',
            name='start_date',
        ),
        migrations.AddField(
            model_name='gateinstallationimage',
            name='gateinstallation_image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDirImage('images/CivilWorksTeam/GateInstallation/')),
        ),
        migrations.CreateModel(
            name='GateInstallationSubtask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('gateinstallation_image_1', models.ImageField(blank=True, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDirSubTask('images/CivilWorksTeam/GateInstallation/'))),
                ('gateinstallation_image_2', models.ImageField(blank=True, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDirSubTask('images/CivilWorksTeam/GateInstallation/'))),
                ('gateinstallation_image_3', models.ImageField(blank=True, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDirSubTask('images/CivilWorksTeam/GateInstallation/'))),
                ('gateinstallation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_casuals_atsite', models.ManyToManyField(blank=True, to='users.Casual')),
                ('project_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BtsSite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GateInstallationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_day', models.DateField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to=erp_core.fileshandler.filemixin.UploadToProjectDirDate('files/Casuals/GateInstallation/'))),
                ('casuals_atsite', models.ManyToManyField(blank=True, to='users.Casual')),
                ('sub_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_construction.GateInstallationSubtask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='gateinstallationimage',
            name='day_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.GateInstallationDate'),
        ),
    ]
