# Generated by Django 2.2.1 on 2019-09-20 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('erp_core', '0002_auto_20190920_0957'),
        ('erp_ftth', '0002_auto_20190920_0957'),
        ('erp_ftts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='pole',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='manholeinstallationimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manholeimages', to='erp_ftts.DailyManHoleInstallation'),
        ),
        migrations.AddField(
            model_name='manholeinstallation',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manholeinstallations', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='manhole',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='manhole',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='interceptionpoint',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interceptionpointftts', to='users.Location'),
        ),
        migrations.AddField(
            model_name='interceptionpoint',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_civil_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsCivilTeam'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_installation_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsInstallationTeam'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_survey',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.fttsSurvey'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttstask',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.Category'),
        ),
        migrations.AddField(
            model_name='fttstask',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssurveyphotos',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssurveyphotos',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fttssurveyphotos', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='ftts_interception_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.InterceptionPoint'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='survey_photos',
            field=models.ManyToManyField(blank=True, to='erp_ftts.fttsSurveyPhotos'),
        ),
        migrations.AddField(
            model_name='fttssubtask',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssubtask',
            name='task_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsTask'),
        ),
        migrations.AddField(
            model_name='fttssite',
            name='ftts_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttssite',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='fttssite',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsprojectpurchaseorder',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='projectpurchaseorders', to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttsproject',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsprocurementteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsprocurementteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttskpi',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsissues',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsissues',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_interception',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.SiteInterception'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_issues',
            field=models.ManyToManyField(blank=True, to='erp_ftts.FttsIssues'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_terminal_in_hse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.SiteTerminalInHse'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_ftts.FttsHealthDocsInstallationTeam'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttshealthdocumentscivilteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsAccessApprovalCivil'),
        ),
        migrations.AddField(
            model_name='fttshealthdocumentscivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttshealthdocumentscivilteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='civilhealthdocuments', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttshealthdocsinstallationteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsAccessApprovalCivil'),
        ),
        migrations.AddField(
            model_name='fttshealthdocsinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttshealthdocsinstallationteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='installationhealthdocuments', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttscommercialteam',
            name='ftts_po_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsProjectPurchaseOrder'),
        ),
        migrations.AddField(
            model_name='fttscommercialteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscommercialteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fttscommercialteams', to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_cable_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.SiteCableInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_duct_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.SiteDuctInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_manhole_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.ManHoleInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_trenching',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.SiteTrenching'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_ftts.FttsHealthDocumentsCivilTeam'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttscertificates',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscertificates',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='ftts_casual',
            field=models.ManyToManyField(related_name='fttscasualregister', to='users.Casual'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttsaccessapprovalinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsaccessapprovalinstallation',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessapprovalcivil', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttsaccessapprovalcivil',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsaccessapprovalcivil',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='civilaccessapproval', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fiberbudget',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='fiberbudget',
            name='site_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='dailysitetrenching',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailysitetrenching',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailysitetrenchings', to='erp_ftts.SiteTrenching'),
        ),
        migrations.AddField(
            model_name='dailysiteterminalinhse',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailysiteterminalinhse',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terminalinhsedays', to='erp_ftts.SiteTerminalInHse'),
        ),
        migrations.AddField(
            model_name='dailysiteinterception',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailysiteinterception',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interceptiondays', to='erp_ftts.SiteInterception'),
        ),
        migrations.AddField(
            model_name='dailysiteductinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailysiteductinstallation',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailyduct', to='erp_ftts.SiteDuctInstallation'),
        ),
        migrations.AddField(
            model_name='dailysitecableinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailysitecableinstallation',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cableinstalldays', to='erp_ftts.SiteCableInstallation'),
        ),
        migrations.AddField(
            model_name='dailymanholeinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailymanholeinstallation',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manholeinstalldays', to='erp_ftts.ManHoleInstallation'),
        ),
        migrations.AddField(
            model_name='dailycivilworkproduction',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='dailycivilworkproduction',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='casualdailyregister',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='casualdailyregister',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite'),
        ),
        migrations.AlterUniqueTogether(
            name='fttssite',
            unique_together={('site_name', 'ftts_project')},
        ),
        migrations.AlterUniqueTogether(
            name='fttscasualdailyregister',
            unique_together={('site_name', 'work_day')},
        ),
        migrations.AlterUniqueTogether(
            name='dailycivilworkproduction',
            unique_together={('site_name', 'work_day')},
        ),
        migrations.AlterUniqueTogether(
            name='casualdailyregister',
            unique_together={('site_name', 'work_day')},
        ),
    ]
