# Generated by Django 2.2.1 on 2019-08-22 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp_ftts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitetrenching',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='sitetrenching',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='sitetrenching',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchings', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='siteterminalinhse',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='siteterminalinhse',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='siteterminalinhse',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='siteterminalinhse', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='sitepoleinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='sitepoleinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='sitepoleinstallation',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitepoleinstallations', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='siteinterception',
            name='manhole',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.ManHole'),
        ),
        migrations.AddField(
            model_name='siteinterception',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='siteinterception',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='siteinterception',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='siteductinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='siteductinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='siteductinstallation',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='siteductinstallation', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='sitecableinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='sitecableinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='sitecableinstallation',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitecableinstallation', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='pole',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='pole',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.AddField(
            model_name='manholeinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='manholeinstallation',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='manholeinstallation',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='manholeinstallations', to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='manhole',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='manhole',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.AddField(
            model_name='interceptionpoint',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='interceptionpointftts', to='users.Location'),
        ),
        migrations.AddField(
            model_name='interceptionpoint',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_civil_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsCivilTeam'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_installation_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsInstallationTeam'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='ftts_survey',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.fttsSurvey'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttssurveyphotos',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssurveyphotos',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='ftts_interception_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.InterceptionPoint'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttssurvey',
            name='survey_photos',
            field=models.ManyToManyField(to='erp_ftts.fttsSurveyPhotos'),
        ),
        migrations.AddField(
            model_name='fttssite',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttssite',
            name='ftts_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttsproject',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsprocurementteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsprocurementteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttsissues',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsissues',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_interception',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.SiteInterception'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_issues',
            field=models.ManyToManyField(blank=True, to='erp_ftts.FttsIssues'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='ftts_terminal_in_hse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.SiteTerminalInHse'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttsinstallationteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttscommercialteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscommercialteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FTTSProject'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_cable_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.SiteCableInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_duct_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.SiteDuctInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_manhole_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.ManHoleInstallation'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_trenching',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.SiteTrenching'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='ftts_casual',
            field=models.ManyToManyField(related_name='fttscasualregister', to='users.Casual'),
        ),
        migrations.AddField(
            model_name='fttscasualdailyregister',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='dailycivilworkproduction',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='dailycivilworkproduction',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='civilworkproduction',
            name='site_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
        ),
        migrations.AddField(
            model_name='casualdailyregister',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='casualdailyregister',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite'),
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
