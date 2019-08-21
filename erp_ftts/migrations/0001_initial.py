# Generated by Django 2.2.1 on 2019-08-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasualDailyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_day', models.DateField(blank=True, null=True)),
                ('work_type', models.CharField(choices=[('T', 'Trenching'), ('B', 'Backfilling'), ('TB', 'Trenching & Backfiling'), ('CI', 'Cable Installation'), ('TBI', 'Trenching & Backfiling &Cable Installation'), ('O', 'Others')], max_length=2)),
                ('others', models.CharField(blank=True, help_text='If work type is others specify the kind of work here', max_length=250, null=True)),
                ('casuals_list_file', models.FileField(upload_to='files/ftts/Casuals/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='CivilWorkProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('trenched_distance', models.FloatField(blank=True, null=True)),
                ('backfilled_distance', models.FloatField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyCivilWorkProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_day', models.DateField(blank=True, null=True)),
                ('trenched_distance', models.FloatField(blank=True, null=True)),
                ('backfilled_distance', models.FloatField(blank=True, null=True)),
                ('duct_installed_length', models.FloatField(blank=True, null=True)),
                ('cable_installed_length', models.FloatField(blank=True, null=True)),
                ('pole_installed', models.IntegerField(blank=True, null=True)),
                ('manhole_installed', models.IntegerField(blank=True, null=True)),
                ('site_dailyproduction_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FTTSCasualDailyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_day', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FttsCivilTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftts_civil_team_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FttsCommercialTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftts_quote', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/quote/%Y/%m/%d/')),
                ('ftts_po_requisition', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/requisition/%Y/%m/%d/')),
                ('ftts_po_requisition_no', models.IntegerField()),
                ('ftts_po_requisition_amount', models.IntegerField()),
                ('ftts_wayleave_application', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/wayleaveapplication/%Y/%m/%d/')),
                ('ftts_project_plan', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/projectplan/%Y/%m/%d/')),
                ('ftts_initial_invoice', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/initialinvoice/%Y/%m/%d/')),
                ('ftts_po_client', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/poclient/%Y/%m/%d/')),
                ('ftts_po_client_no', models.IntegerField()),
                ('ftts_po_client_amount', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FttsInstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('casuals_list', models.FileField(blank=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('ftts_integration', models.BooleanField(default=False)),
                ('ftts_installation_team_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('ftts_asbuit_received', models.BooleanField(default=True)),
                ('snag_document', models.FileField(blank=True, null=True, upload_to='files/SafaricomTeamftts/snag/%Y/%m/%d/')),
                ('snag_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('conditional_acceptance_cert', models.FileField(blank=True, null=True, upload_to='files/SafaricomTeamftts/conditionalcert/%Y/%m/%d/')),
                ('conditional_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FttsIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftts_issue', models.CharField(max_length=100)),
                ('ftts_issue_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeamFtts/issues/%Y/%m/%d/')),
                ('ftts_issue_sorted_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeamFtts/issues/%Y/%m/%d/')),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FttsProcurementTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftts_material_requisition', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/materialrequisition/%Y/%m/%d/')),
                ('ftts_po_quote_serviceno', models.IntegerField()),
                ('ftts_po_quote_serviceamount', models.IntegerField()),
                ('ftts_po_subcontractors', models.FileField(blank=True, null=True, upload_to='files/ftts/CommercialTeam/posubcontractors/%Y/%m/%d/')),
                ('ftts_po_quote_subconamount', models.IntegerField()),
                ('ftts_po_quote_subconno', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FTTSProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('ftts_final_acceptance_cert', models.FileField(blank=True, null=True, upload_to='FTTS/files/SafaricomTeamftts/finalcert/%Y/%m/%d/')),
                ('ftts_final_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('ftts_accumulated_BOM_survey', models.FileField(blank=True, null=True, upload_to='FTTS/files/accumulatedBOM/%Y/%m/%d/')),
                ('ftts_accumulated_BOM_survey_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FttsSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('site_name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='fttsSurvey',
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
                ('high_level_design', models.FileField(blank=True, null=True, upload_to='files/ftts/survey/highleveldesigns/%Y/%m/%d/')),
                ('survey_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='fttsSurveyPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('survey_image_1', models.ImageField(upload_to='images/ftts/survey/%Y/%m/%d/')),
                ('survey_image_2', models.ImageField(blank=True, null=True, upload_to='images/ftts/survey/%Y/%m/%d/')),
                ('survey_image_3', models.ImageField(blank=True, null=True, upload_to='images/ftts/survey/%Y/%m/%d/')),
                ('survey_images_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FttsTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterceptionPoint',
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
            name='ManHole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('manhole_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ManHoleInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('manhole_image_1', models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')),
                ('manhole_image_2', models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')),
                ('manhole_image_3', models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')),
                ('manhole_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('pole_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteCableInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_cable_installation_image_1', models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('site_cable_installation_image_2', models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('site_cable_installation_image_3', models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('site_cable_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteDuctInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_duct_installation_image_1', models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')),
                ('site_duct_installation_image_2', models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')),
                ('site_duct_installation_image_3', models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')),
                ('site_duct_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteInterception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_interception_image_1', models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')),
                ('site_interception_image_2', models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')),
                ('site_interception_image_3', models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')),
                ('site_interception_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SitePoleInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_pole_installation_image_1', models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('site_pole_installation_image_2', models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('site_pole_installation_image_3', models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('site_pole_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteTerminalInHse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_terminal_in_hse_image_1', models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')),
                ('site_terminal_in_hse_image_2', models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')),
                ('site_terminal_in_hse_image_3', models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')),
                ('site_terminal_in_hse_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteTrenching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/ftts/Casuals/poleinstallation/%Y/%m/%d/')),
                ('site_trenching_image_1', models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('site_trenching_image_2', models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('site_trenching_image_3', models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('distance_trenched', models.FloatField(blank=True, null=True)),
                ('site_trenching_comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
