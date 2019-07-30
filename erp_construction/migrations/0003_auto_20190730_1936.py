# Generated by Django 2.2.1 on 2019-07-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0002_auto_20190730_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antennacoaxinstallimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='bindingimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='blockworkpanelconstimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='boundarywallimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='bs241andgeneatorslabsimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='bs241concretepourcuringperiodimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='btsinstallationtask',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='cablewaysimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='civilworksteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_construction.HealthDocumentsCivilTeam'),
        ),
        migrations.AlterField(
            model_name='concretecuringperiodimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='concretepourimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='electricalearthing',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='electricaltasks',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='excavationimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='foundationimage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='foundfootpourimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='gateinstallationimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='generatorinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='installationteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, to='erp_construction.HealthDocumentsInstallationTeam'),
        ),
        migrations.AlterField(
            model_name='kplcsolarimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='mwinstallationtask',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='razorelectricfenceimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='reticulationapsinstallation',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='setsiteclearingimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='steelfixformworkimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='telecomtasks',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='towerantennacoaximage',
            name='engineers_atsite',
            field=models.ManyToManyField(blank=True, to='users.Engineer'),
        ),
        migrations.AlterField(
            model_name='towerbaseimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='towererectionimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='towerpaintimage',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AlterField(
            model_name='undergroundtasks',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
    ]
