# Generated by Django 2.2.1 on 2019-05-28 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessApprovalCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_approval', models.FileField(upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')),
                ('access_approval_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccessApprovalInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_approval', models.FileField(upload_to='files/InstallationTeam/accessapproval/%Y/%m/%d/')),
                ('access_approval_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BindingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binding_image_1', models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')),
                ('binding_image_2', models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')),
                ('binding_image_3', models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')),
                ('binding_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BTSAndGeneatorSlabsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bts_and_generator_slabs_image_1', models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')),
                ('bts_and_generator_slabs_image_2', models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')),
                ('bts_and_generator_slabs_image_3', models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')),
                ('bts_and_generator_slabs_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConcretePourCuringImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concrete_pour_curing_image_1', models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')),
                ('concrete_pour_curing_image_2', models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')),
                ('concrete_pour_curing_image_3', models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')),
                ('concrete_pour_curing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElectricalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electrical_installation_image_1', models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')),
                ('electrical_installation_image_2', models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')),
                ('electrical_installation_image_3', models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')),
                ('electrical_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthDocumentsInstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_hazard_form', models.FileField(upload_to='files/HealthDocumentsInstallationTeam/jobhazard/%Y/%m/%d/')),
                ('job_hazard_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('incident_notification_form', models.FileField(upload_to='files/HealthDocumentsInstallationTeam/incident/%Y/%m/%d/')),
                ('incident_notification_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('toolbox_meeting_form', models.FileField(upload_to='files/HealthDocumentsInstallationTeam/toolbox/%Y/%m/%d/')),
                ('toolbox_meeting_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('communication_plan_form', models.FileField(upload_to='files/HealthDocumentsInstallationTeam/communication/%Y/%m/%d/')),
                ('communication_plan_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('health_documents_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('site_number', models.CharField(max_length=100, unique=True)),
                ('BTS_type', models.CharField(max_length=100)),
                ('site_owner', models.CharField(max_length=100)),
                ('geotech_file', models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/')),
                ('access_letter', models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/')),
                ('approved_drawing', models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIcons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/Project/Icons/%Y/%m/%d/')),
                ('site_owner', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TowerBaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towerbase_image_1', models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')),
                ('towerbase_image_2', models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')),
                ('towerbase_image_3', models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')),
                ('tower_base_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SteelFixFormworkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steel_fix_formwork_image_1', models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')),
                ('steel_fix_formwork_image_2', models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')),
                ('steel_fix_formwork_image_3', models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')),
                ('steel_fix_formwork_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SiteWallingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_walling_image_1', models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')),
                ('site_walling_image_2', models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')),
                ('site_walling_image_3', models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')),
                ('site_walling_images_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SetSiteClearingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_site_clearing_image_1', models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')),
                ('setting_site_clearing_image_2', models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')),
                ('setting_site_clearing_image_3', models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')),
                ('setting_site_clearing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='RFAndLinkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rf_and_link_installation_image_1', models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')),
                ('rf_and_link_installation_image_2', models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')),
                ('rf_and_link_installation_image_3', models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')),
                ('rf_and_link_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPurchaseOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_file', models.FileField(blank=True, null=True, upload_to='files/CommercialTeam/pofile/%Y/%m/%d/')),
                ('material_cost', models.IntegerField()),
                ('labour_cost', models.IntegerField()),
                ('total_cost_of_po', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_costing_file', models.FileField(blank=True, null=True, upload_to='files/CommercialTeam/projectcosting/%Y/%m/%d/')),
                ('material_cost', models.IntegerField()),
                ('labour_cost', models.IntegerField()),
                ('total_projected_cost', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ProjectIcons'),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location'),
        ),
        migrations.CreateModel(
            name='ProcurementTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_steel', models.FileField(blank=True, null=True, upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/')),
                ('po_steel_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('po_electrical_materials', models.FileField(blank=True, null=True, upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/')),
                ('po_electrical_materials_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('po_subcontractors', models.FileField(blank=True, null=True, upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/')),
                ('po_subcontractors_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='KPLCSolarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kplc_solar_installation_image_1', models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')),
                ('kplc_solar_installation_image_2', models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')),
                ('kplc_solar_installation_image_3', models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')),
                ('kplc_solar_installation_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='InstallationTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signoff', models.FileField(upload_to='files/SafaricomTeam/signoff/%Y/%m/%d/')),
                ('signoff_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('rf_document', models.FileField(upload_to='files/SafaricomTeam/rf/%Y/%m/%d/')),
                ('rf_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('integration_parameter', models.BooleanField(default=False)),
                ('integration_parameter_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('snag_document', models.FileField(upload_to='files/SafaricomTeam/snag/%Y/%m/%d/')),
                ('snag_document_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('conditional_acceptance_cert', models.FileField(upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/')),
                ('conditional_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('final_acceptance_cert', models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/')),
                ('final_acceptance_cert_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('access_approvals_field', models.ManyToManyField(to='erp_construction.AccessApprovalInstallation')),
                ('electrical_installation_images', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ElectricalImage')),
                ('health_documents', models.ManyToManyField(to='erp_construction.HealthDocumentsInstallationTeam')),
                ('kplc_solar_installation_images', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.KPLCSolarImage')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
                ('rf_and_link_installation_images', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.RFAndLinkImage')),
            ],
        ),
        migrations.AddField(
            model_name='healthdocumentsinstallationteam',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.CreateModel(
            name='HealthDocumentsCivilTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_hazard_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/jobhazard/%Y/%m/%d/')),
                ('job_hazard_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('incident_notification_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/incident/%Y/%m/%d/')),
                ('incident_notification_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('toolbox_meeting_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/toolbox/%Y/%m/%d/')),
                ('toolbox_meeting_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('communication_plan_form', models.FileField(upload_to='files/HealthDocumentsCivilTeam/communication/%Y/%m/%d/')),
                ('communication_plan_form_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('health_documents_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='FoundationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foundation_and_curing_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('binding', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BindingImage')),
                ('concrete_pour_curing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.ConcretePourCuringImage')),
                ('excavation_tower_base', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.TowerBaseImage')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
                ('setting_site_clearing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SetSiteClearingImage')),
                ('steel_fix_formwork', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SteelFixFormworkImage')),
            ],
        ),
        migrations.AddField(
            model_name='electricalimage',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='concretepourcuringimage',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.CreateModel(
            name='CommercialTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_quote_file', models.FileField(upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/')),
                ('approved_quote_amount', models.IntegerField()),
                ('initial_invoice', models.FileField(blank=True, null=True, upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/')),
                ('initial_invoice_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('po_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ProjectPurchaseOrders')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('project_costing_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_construction.ProjectCosting')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
            ],
        ),
        migrations.CreateModel(
            name='CivilWorksTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('access_approvals_field', models.ManyToManyField(to='erp_construction.AccessApprovalCivil')),
                ('bts_and_generator_slabs_images', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BTSAndGeneatorSlabsImage')),
                ('foundation_and_curing_images', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.FoundationImage')),
                ('health_documents', models.ManyToManyField(to='erp_construction.HealthDocumentsCivilTeam')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project')),
                ('site_walling_images_field', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.SiteWallingImage')),
            ],
        ),
        migrations.AddField(
            model_name='btsandgeneatorslabsimage',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='bindingimage',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='accessapprovalinstallation',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
        migrations.AddField(
            model_name='accessapprovalcivil',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.Project'),
        ),
    ]
