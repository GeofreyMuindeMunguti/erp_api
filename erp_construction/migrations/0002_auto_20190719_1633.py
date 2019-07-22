# Generated by Django 2.2.1 on 2019-07-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warrantycertificate',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='warrantycertificate',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='undergroundtasks',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='undergroundtasks',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='towerpaintimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='towerpaintimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='towererectionimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='towererectionimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='towerbaseimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='towerbaseimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='antenna_coax_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.AntennaCoaxInstallImage'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='cable_ways',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.CableWaysImage'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='tower_erection',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TowerErectionImage'),
        ),
        migrations.AddField(
            model_name='towerantennacoaximage',
            name='tower_painting',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TowerPaintImage'),
        ),
        migrations.AddField(
            model_name='testcetificate',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='testcetificate',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='telecomtasks',
            name='Installation_of_BTS',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.BTSinstallationTask'),
        ),
        migrations.AddField(
            model_name='telecomtasks',
            name='Installation_of_MW_links',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.MWInstallationTask'),
        ),
        migrations.AddField(
            model_name='telecomtasks',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='telecomtasks',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='task',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Category'),
        ),
        migrations.AddField(
            model_name='task',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='subtask',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='subtask',
            name='task_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Task'),
        ),
        migrations.AddField(
            model_name='steelfixformworkimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='steelfixformworkimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='setSiteclearingimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='setSiteclearingimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='reticulationapsinstallation',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='reticulationapsinstallation',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='razorelectricfenceimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='razorelectricfenceimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='projectpurchaseorders',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='projectcosting',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SiteIcons'),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.AddField(
            model_name='procurementteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='procurementteam',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='mwinstallationtask',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='mwinstallationtask',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='kplcsolarimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='kplcsolarimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='issues',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='issues',
            name='Site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='electrical_tasks_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ElectricalTasks'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, null=True, to='erp_construction.HealthDocumentsInstallationTeam'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='issues',
            field=models.ManyToManyField(blank=True, to='erp_construction.Issues'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='installationteam',
            name='telecom_tasks_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TelecomTasks'),
        ),
        migrations.AddField(
            model_name='healthdocumentsinstallationteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.AccessApprovalInstallation'),
        ),
        migrations.AddField(
            model_name='healthdocumentsinstallationteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='healthdocumentsinstallationteam',
            name='Site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='healthdocumentscivilteam',
            name='access_approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.AccessApprovalCivil'),
        ),
        migrations.AddField(
            model_name='healthdocumentscivilteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='healthdocumentscivilteam',
            name='Site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='healthdocumentscivilteam', to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='generatorinstallation',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='generatorinstallation',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='gateinstallationimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='gateinstallationimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='foundfootpourimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='foundfootpourimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='binding',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BindingImage'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='concrete_curing_period',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ConcreteCuringPeriodImage'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='concrete_pour_curing_period',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ConcretePourImage'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='excavation_tower_base',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TowerBaseImage'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='setting_Site_clearing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SetSiteClearingImage'),
        ),
        migrations.AddField(
            model_name='foundationimage',
            name='steel_fix_formwork',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SteelFixFormworkImage'),
        ),
        migrations.AddField(
            model_name='excavationimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='excavationimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='Earthing_connections_and_testing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ElectricalEarthing'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='Electricalreticulation_APSInstallation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ReticulationAPSinstallation'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='Generator_and_Fuel_Tank_Installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.GeneratorInstallation'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='KPLC_solar_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.KPLCSolarImage'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='Underground_ducting_and_manholes',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.UndergroundTasks'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='electricaltasks',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='electricalearthing',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='electricalearthing',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='concretepourimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='concretepourimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='concretecuringperiodimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='concretecuringperiodimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='commercialteam',
            name='po_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ProjectPurchaseOrders'),
        ),
        migrations.AddField(
            model_name='commercialteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='commercialteam',
            name='project_costing_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ProjectCosting'),
        ),
        migrations.AddField(
            model_name='commercialteam',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='bs241_and_generator_slabs_images',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BS241AndGeneatorSlabsImage'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='foundation_and_curing_images',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.FoundationImage'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='health_documents',
            field=models.ManyToManyField(blank=True, null=True, to='erp_construction.HealthDocumentsCivilTeam'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='Site_walling_images_field',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BoundaryWallImage'),
        ),
        migrations.AddField(
            model_name='civilworksteam',
            name='tower_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TowerAntennaCoaxImage'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='cablewaysimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='cablewaysimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='btsinstallationtask',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='btsinstallationtask',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='bs241concretepourcuringperiodimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='bs241concretepourcuringperiodimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='bs241andgeneatorslabsimage',
            name='bs241_concrete_pour_pouring_period',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BS241ConcretePourCuringPeriodImage'),
        ),
        migrations.AddField(
            model_name='bs241andgeneatorslabsimage',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='bs241andgeneatorslabsimage',
            name='foundation_foot_pouring',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ExcavationImage'),
        ),
        migrations.AddField(
            model_name='bs241andgeneatorslabsimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='block_construction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BlockworkPanelConstImage'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='engineers_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Engineer'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='foundation_foot_pouring',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.FoundFootPourImage'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='gate_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.GateInstallationImage'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='boundarywallimage',
            name='razor_electric_fence',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.RazorElectricFenceImage'),
        ),
        migrations.AddField(
            model_name='blockworkpanelconstimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='blockworkpanelconstimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='bindingimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='bindingimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='antennacoaxinstallimage',
            name='no_of_casuals_atSite',
            field=models.ManyToManyField(blank=True, null=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='antennacoaxinstallimage',
            name='Site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='accessapprovalinstallation',
            name='Site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='accessapprovalcivil',
            name='Site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='accessapprovalcivil', to='erp_construction.Project'),
        ),
    ]
