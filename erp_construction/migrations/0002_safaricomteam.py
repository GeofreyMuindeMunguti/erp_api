# Generated by Django 2.2.1 on 2019-05-06 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafaricomTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signoff_and_rf_document', models.FileField(upload_to='files/SafaricomTeam/rfsignoff/%Y/%m/%d/')),
                ('signoff_and_rf_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('integration_parameter', models.FileField(upload_to='files/SafaricomTeam/integrationparameters/%Y/%m/%d/')),
                ('integration_parameter_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('snag_document', models.FileField(upload_to='files/SafaricomTeam/snag/%Y/%m/%d/')),
                ('snag_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('conditional_acceptance_cert', models.FileField(upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/')),
                ('conditional_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('final_acceptance_cert', models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/')),
                ('final_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.User')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
    ]
