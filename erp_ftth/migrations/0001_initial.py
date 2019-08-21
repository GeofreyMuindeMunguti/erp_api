# Generated by Django 2.2.1 on 2019-08-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FtthBackfilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftth/Casuals/FtthBackfilling/%Y/%m/%d/')),
                ('ftth_backfilling_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthCableInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftth/Casuals/FtthBackfilling/%Y/%m/%d/')),
                ('ftth_cable_installation_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthCivilTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftth_civil_team_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthCommercialTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_boq', models.FileField(blank=True, null=True, upload_to='files/ftth/CommercialTeam/boq/%Y/%m/%d/')),
                ('ftth_quote', models.FileField(blank=True, null=True, upload_to='files/ftth/CommercialTeam/quote/%Y/%m/%d/')),
                ('ftth_wayleave_application', models.FileField(blank=True, null=True, upload_to='files/ftth/CommercialTeam/wayleaveapplication/%Y/%m/%d/')),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthCoreProvision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_core_provision_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthInstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_installation_team_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('ftth_asbuit_received', models.BooleanField(default=True)),
                ('snag_document', models.FileField(blank=True, null=True, upload_to='files/SafaricomTeamftth/snag/%Y/%m/%d/')),
                ('snag_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('conditional_acceptance_cert', models.FileField(blank=True, null=True, upload_to='files/SafaricomTeamftth/conditionalcert/%Y/%m/%d/')),
                ('conditional_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthInterceptionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('interception_point_name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_issue', models.CharField(max_length=100)),
                ('ftth_issue_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeamFtth/issues/%Y/%m/%d/')),
                ('ftth_issue_sorted_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeamFtth/issues/%Y/%m/%d/')),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthOTDRTraces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_otdr_traces_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthPoleInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftth/Casuals/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthPowerLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_power_level_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthProcurementTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_bom', models.FileField(blank=True, null=True, upload_to='files/ftth/CommercialTeam/bom/%Y/%m/%d/')),
                ('ftth_initial_invoice', models.FileField(blank=True, null=True, upload_to='files/ftth/CommercialTeam/initialinvoice/%Y/%m/%d/')),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FTTHProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('initial_kmz', models.FileField(blank=True, null=True, upload_to='files/ftth/InitialKMZ/%Y/%m/%d/')),
                ('ftts_final_acceptance_cert', models.FileField(blank=True, null=True, upload_to='files/ftth/SafaricomTeamftth/finalcert/%Y/%m/%d/')),
                ('ftts_final_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_acknowledged', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FtthSignalTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_signal_testing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthSplicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_splicing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthSplicingEnclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_encore_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthSplicingFAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_fat_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthSplicingFDT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_fdt_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ftthSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('site_latitude', models.FloatField()),
                ('site_longitude', models.FloatField()),
                ('distance_from_ip', models.FloatField(blank=True, null=True)),
                ('high_level_design', models.FileField(blank=True, null=True, upload_to='files/ftth/survey/highleveldesigns/%Y/%m/%d/')),
                ('ftth_survey_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ftthSurveyPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('survey_image_1', models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/')),
                ('survey_image_2', models.ImageField(blank=True, null=True, upload_to='images/ftth/survey/%Y/%m/%d/')),
                ('survey_image_3', models.ImageField(blank=True, null=True, upload_to='images/ftth/survey/%Y/%m/%d/')),
                ('survey_images_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FtthTrenching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftth/Casuals/FtthTrenching/%Y/%m/%d/')),
                ('ftth_trenching_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
