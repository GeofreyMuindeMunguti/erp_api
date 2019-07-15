# Generated by Django 2.2.1 on 2019-07-15 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antennacoaxinstallimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='bindingimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='blockworkpanelconstimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='boundarywallimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='bs241andgeneatorslabsimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='bs241concretepourcuringperiodimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='btsinstallationtask',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='cablewaysimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='civilworksteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, null=True, to='erp_construction.HealthDocumentsCivilTeam'),
        ),
        migrations.AlterField(
            model_name='concretecuringperiodimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='concretepourimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='electricalearthing',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='electricaltasks',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='excavationimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='foundationimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='foundfootpourimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='gateinstallationimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='generatorinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='installationteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, null=True, to='erp_construction.HealthDocumentsInstallationTeam'),
        ),
        migrations.AlterField(
            model_name='kplcsolarimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='mwinstallationtask',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mwinstallationtask',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='project',
            name='BTS_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='access_letter',
            field=models.FileField(blank=True, null=True, upload_to='files/Project/accessletters/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_drawing',
            field=models.FileField(blank=True, null=True, upload_to='files/Project/approveddrawings/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='geotech_file',
            field=models.FileField(blank=True, null=True, upload_to='files/Project/geotech/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='site_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='site_owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='razorelectricfenceimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='reticulationapsinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='setsiteclearingimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='steelfixformworkimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='telecomtasks',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='towerantennacoaximage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='towerbaseimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='towererectionimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='towerpaintimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='undergroundtasks',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
    ]
