# Generated by Django 2.2.1 on 2019-09-15 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp_ftth', '0001_initial'),
        ('users', '0001_initial'),
        ('erp_core', '0002_category_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ftthtrenching',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthtrenching',
            name='project_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ftthtrenchings', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthteam',
            name='ftth_civil_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthCivilTeam'),
        ),
        migrations.AddField(
            model_name='ftthteam',
            name='ftth_installation_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthInstallationTeam'),
        ),
        migrations.AddField(
            model_name='ftthteam',
            name='ftth_survey',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.ftthSurvey'),
        ),
        migrations.AddField(
            model_name='ftthteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthteam',
            name='project_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthtask',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.Category'),
        ),
        migrations.AddField(
            model_name='ftthtask',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsurveyphotos',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsurveyphotos',
            name='project_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsurvey',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='ftthsurvey',
            name='ftth_interception_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthInterceptionPoint'),
        ),
        migrations.AddField(
            model_name='ftthsurvey',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsurvey',
            name='project_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsurvey',
            name='survey_photos',
            field=models.ManyToManyField(blank=True, to='erp_ftth.ftthSurveyPhotos'),
        ),
        migrations.AddField(
            model_name='ftthsubtask',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsubtask',
            name='task_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftth.FtthTask'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfdtimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingFDTimage', to='erp_ftth.DailyFtthSplicingFDT'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfdt',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfdt',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthsplicingfdts', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfatimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingFATimage', to='erp_ftth.DailyFtthSplicingFAT'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfat',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsplicingfat',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthsplicingfat', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsplicingenclosureimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingenclosureimage', to='erp_ftth.DailyFtthSplicingEnclosure'),
        ),
        migrations.AddField(
            model_name='ftthsplicingenclosure',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsplicingenclosure',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthsplicingenclosures', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsplicing',
            name='ftth_splicing_encore',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthSplicingEnclosure'),
        ),
        migrations.AddField(
            model_name='ftthsplicing',
            name='ftth_splicing_fat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthSplicingFAT'),
        ),
        migrations.AddField(
            model_name='ftthsplicing',
            name='ftth_splicing_fdt',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthSplicingFDT'),
        ),
        migrations.AddField(
            model_name='ftthsplicing',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsplicing',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthsignaltesting',
            name='ftth_core_provision',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthCoreProvision'),
        ),
        migrations.AddField(
            model_name='ftthsignaltesting',
            name='ftth_otdr_traces',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthOTDRTraces'),
        ),
        migrations.AddField(
            model_name='ftthsignaltesting',
            name='ftth_power_levels',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthPowerLevels'),
        ),
        migrations.AddField(
            model_name='ftthsignaltesting',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthsignaltesting',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthproject',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthprocurementteam',
            name='po_to_supplier',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthPoToSupplier'),
        ),
        migrations.AddField(
            model_name='ftthprocurementteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthprocurementteam',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthpowerlevelsimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='powerlevelsimage', to='erp_ftth.DailyFtthPowerLevels'),
        ),
        migrations.AddField(
            model_name='ftthpowerlevels',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthpowerlevels',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthpowerlevels', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthpotosupplier',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthpotosupplier',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthpoleinstallationimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poleinstallationimage', to='erp_ftth.DailyFtthPoleInstallation'),
        ),
        migrations.AddField(
            model_name='ftthpoleinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthpoleinstallation',
            name='project_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ftthpoleinstallations', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthotdrtracesimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OTDRTracesimage', to='erp_ftth.DailyFtthOTDRTraces'),
        ),
        migrations.AddField(
            model_name='ftthotdrtraces',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthotdrtraces',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otdrtrace', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthkpi',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthissues',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthissues',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthinterceptionpoint',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='ftthinterceptionpoint',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='ftth_issues',
            field=models.ManyToManyField(blank=True, to='erp_ftth.FtthIssues'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='ftth_signal_testing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthSignalTesting'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='ftth_splicing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthSplicing'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_ftth.FtthHealthDocsInstallationTeam'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthinstallationteam',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocumentscivilteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthAccessApprovalCivil'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocumentscivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocumentscivilteam',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthcivilhealthdocuments', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocsinstallationteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthAccessApprovalInstallation'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocsinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthhealthdocsinstallationteam',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthinstallationhealthdocuments', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthcoreprovisionimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coreprovisionimage', to='erp_ftth.DailyFtthCoreProvision'),
        ),
        migrations.AddField(
            model_name='ftthcoreprovision',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthcoreprovision',
            name='project_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthcommercialteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthcommercialteam',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='ftth_backfiling',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthBackfilling'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='ftth_cable_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthCableInstallation'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='ftth_pole_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthPoleInstallation'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='ftth_trenching',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FtthTrenching'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_ftth.FtthHealthDocumentsCivilTeam'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthcivilteam',
            name='project_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthcertificates',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthcertificates',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthcableinstallationimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cableinstallationimage', to='erp_ftth.DailyFtthCableInstallation'),
        ),
        migrations.AddField(
            model_name='ftthcableinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthcableinstallation',
            name='project_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ftthcableinstallations', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthbackfillingimage',
            name='day_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftthbackfillingimages', to='erp_ftth.DailyFtthBackfilling'),
        ),
        migrations.AddField(
            model_name='ftthbackfilling',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthbackfilling',
            name='project_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='ftthbackfillings', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthaccessapprovalinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthaccessapprovalinstallation',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthaccessapprovalinstallation', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='ftthaccessapprovalcivil',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='ftthaccessapprovalcivil',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ftthcivilaccessapproval', to='erp_ftth.FTTHProject'),
        ),
        migrations.AddField(
            model_name='dailyftthtrenching',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthtrenching',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftthtrenchingdays', to='erp_ftth.FtthTrenching'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingfdt',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingfdt',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingFDT', to='erp_ftth.FtthSplicingFDT'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingfat',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingfat',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingFAT', to='erp_ftth.FtthSplicingFAT'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingenclosure',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthsplicingenclosure',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splicingencore', to='erp_ftth.FtthSplicingEnclosure'),
        ),
        migrations.AddField(
            model_name='dailyftthpowerlevels',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthpowerlevels',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftthpowerlevelsdays', to='erp_ftth.FtthPowerLevels'),
        ),
        migrations.AddField(
            model_name='dailyftthpoleinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthpoleinstallation',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poleinstallationdays', to='erp_ftth.FtthPoleInstallation'),
        ),
        migrations.AddField(
            model_name='dailyftthotdrtraces',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthotdrtraces',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OTDRTraces', to='erp_ftth.FtthOTDRTraces'),
        ),
        migrations.AddField(
            model_name='dailyftthcoreprovision',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthcoreprovision',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coreprovision', to='erp_ftth.FtthCoreProvision'),
        ),
        migrations.AddField(
            model_name='dailyftthcableinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthcableinstallation',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cableinstallation', to='erp_ftth.FtthCableInstallation'),
        ),
        migrations.AddField(
            model_name='dailyftthbackfilling',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='dailyftthbackfilling',
            name='sub_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftthbackfillingdays', to='erp_ftth.FtthBackfilling'),
        ),
    ]
