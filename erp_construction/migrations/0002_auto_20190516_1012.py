# Generated by Django 2.2.1 on 2019-05-16 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessapprovalinstallation',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='btsandgeneatorslabsimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='access_approvals_field',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='bts_and_generator_slabs_images',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='foundation_and_curing_images',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='health_documents',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='civilworksteam',
            name='site_walling_images_field',
        ),
        migrations.RemoveField(
            model_name='commercialteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='commercialteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='electricalimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='foundationimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='healthdocumentscivilteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='healthdocumentscivilteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='healthdocumentsinstallationteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='healthdocumentsinstallationteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='access_approvals_field',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='electrical_installation_images',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='health_documents',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='kplc_solar_installation_images',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='installationteam',
            name='rf_and_link_installation_images',
        ),
        migrations.RemoveField(
            model_name='kplcsolarimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='procurementteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='procurementteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='rfandlinkimage',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='safaricomteam',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='safaricomteam',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='sitewallingimage',
            name='project_name',
        ),
        migrations.DeleteModel(
            name='AccessApprovalCivil',
        ),
        migrations.DeleteModel(
            name='AccessApprovalInstallation',
        ),
        migrations.DeleteModel(
            name='BTSAndGeneatorSlabsImage',
        ),
        migrations.DeleteModel(
            name='CivilWorksTeam',
        ),
        migrations.DeleteModel(
            name='CommercialTeam',
        ),
        migrations.DeleteModel(
            name='ElectricalImage',
        ),
        migrations.DeleteModel(
            name='FoundationImage',
        ),
        migrations.DeleteModel(
            name='HealthDocumentsCivilTeam',
        ),
        migrations.DeleteModel(
            name='HealthDocumentsInstallationTeam',
        ),
        migrations.DeleteModel(
            name='InstallationTeam',
        ),
        migrations.DeleteModel(
            name='KPLCSolarImage',
        ),
        migrations.DeleteModel(
            name='ProcurementTeam',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='RFAndLinkImage',
        ),
        migrations.DeleteModel(
            name='SafaricomTeam',
        ),
        migrations.DeleteModel(
            name='SiteWallingImage',
        ),
    ]
