# Generated by Django 2.2.1 on 2019-05-06 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0005_auto_20190506_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilworksteam',
            name='foundation_and_curing_images',
        ),
        migrations.CreateModel(
            name='HealthDocumentsInstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_hazard_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/%Y/%m/%d/')),
                ('job_hazard_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('incident_notification_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/%Y/%m/%d/')),
                ('incident_notification_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('toolbox_meeting_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/%Y/%m/%d/')),
                ('toolbox_meeting_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('communication_plan_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/%Y/%m/%d/')),
                ('communication_plan_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.User')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='FoundationImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foundation_and_curing_image', models.ImageField(upload_to='images/CivilWorksTeam/foundation/%Y/%m/%d/')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='foundation_and_curing_images',
            field=models.ManyToManyField(to='erp_construction.FoundationImages'),
        ),
    ]
