# Generated by Django 2.2.1 on 2019-07-24 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
        ('users', '0001_initial'),
        ('erp_fiber_ftth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FtthBackfilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_backfilling_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')),
                ('ftth_backfilling_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthCableInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_cable_installation_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')),
                ('ftth_cable_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthCoreProvision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_core_provision_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')),
                ('ftth_core_provision_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthOTDRTraces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_otdr_traces_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')),
                ('ftth_otdr_traces_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthPowerLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_power_level_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')),
                ('ftth_power_level_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthTrenching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_trenching_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_image_2', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_image_3', models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('ftth_trenching_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthSplicingFDT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_fdt_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')),
                ('ftth_splicing_fdt_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthSplicingFAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_fat_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')),
                ('ftth_splicing_fat_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthSplicingEnclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_splicing_encore_image_1', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_image_2', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_image_3', models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')),
                ('ftth_splicing_encore_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthSplicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_splicing_encore', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthSplicingEnclosure')),
                ('ftth_splicing_fat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthSplicingFAT')),
                ('ftth_splicing_fdt', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthSplicingFDT')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthSignalTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_splicing_encore', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthCoreProvision')),
                ('ftth_splicing_fat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthPowerLevels')),
                ('ftth_splicing_fdt', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthOTDRTraces')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthPoleInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ftth_pole_installation_image_1', models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_image_2', models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_image_3', models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')),
                ('ftth_pole_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthInstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_signal_testing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthSignalTesting')),
                ('ftth_splicing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthSplicing')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthCivilTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ftth_backfiling', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthBackfilling')),
                ('ftth_cable_installation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthCableInstallation')),
                ('ftth_pole_installation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthPoleInstallation')),
                ('ftth_trenching', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftth.FtthTrenching')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
        migrations.CreateModel(
            name='FtthAsBuilt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftth_asbuit_received', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Site')),
            ],
        ),
    ]
