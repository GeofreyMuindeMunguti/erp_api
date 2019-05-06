# Generated by Django 2.2.1 on 2019-05-06 08:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcurementTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_steel', models.FileField(upload_to='files/ProcurementTeam/%Y/%m/%d/')),
                ('po_steel_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('po_electrical_materials', models.FileField(upload_to='files/ProcurementTeam/%Y/%m/%d/')),
                ('po_electrical_materials_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('po_subcontractors', models.FileField(upload_to='files/ProcurementTeam/%Y/%m/%d/')),
                ('po_subcontractors_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.User')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='HealthDocumentsCivilTeam',
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
            name='CivilWorksTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_documents_comment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=None)),
                ('access_approval', models.FileField(upload_to='files/CivilWorksTeam/%Y/%m/%d/')),
                ('access_approval_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('foundation_and_curing_images', models.ImageField(upload_to='images/CivilWorksTeam/foundation/%Y/%m/%d/')),
                ('foundation_and_curing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('bts_and_generator_slabs_images', models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')),
                ('bts_and_generator_slabs_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('site_walling_images', models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')),
                ('site_walling_images_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('health_documents', models.ManyToManyField(to='erp_construction.HealthDocumentsCivilTeam')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.User')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
    ]
