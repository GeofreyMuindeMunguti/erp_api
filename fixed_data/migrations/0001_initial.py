# Generated by Django 2.2.1 on 2019-09-20 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveFiberInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActiveFiberPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveFibertestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('management_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('management_vlan', models.IntegerField(blank=True, null=True)),
                ('confiqured_ar_interface', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, help_text='Tag No', null=True, upload_to='files/Fixed_data/ActiveFiber/')),
                ('router_type', models.CharField(blank=True, max_length=150, null=True)),
                ('router_model', models.IntegerField(blank=True, null=True)),
                ('router_SNMP_CMP_enable', models.BooleanField(default=False)),
                ('lan_status', models.BooleanField(default=True)),
                ('power_status', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.CharField(blank=True, max_length=150, null=True)),
                ('longitude', models.CharField(blank=True, max_length=150, null=True)),
                ('building_image_1', models.ImageField(blank=True, null=True, upload_to='images/Fixed_data/building/')),
                ('building_image_2', models.ImageField(blank=True, null=True, upload_to='images/Fixed_data/building/')),
                ('fiber_ready', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CeragonInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CeragonPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CeragontestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('hsu_pss', models.IntegerField(blank=True, null=True)),
                ('hsu_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('vlan', models.GenericIPAddressField(blank=True, null=True)),
                ('connecting_bts', models.CharField(blank=True, max_length=150, null=True)),
                ('aggregation', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='files/Fixed_data/Ceragon/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=150)),
                ('second_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('phone_no', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_by',),
            },
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('item', models.CharField(blank=True, max_length=250, null=True)),
                ('quantity', models.FloatField(default=0)),
                ('unit_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fiberinstallations', to='fixed_data.Consumable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('circuit_id', models.IntegerField(unique=True)),
                ('survey_file', models.FileField(blank=True, null=True, upload_to='files/Fixed_data/surveyfile/')),
                ('decomisioned', models.BooleanField(default=False)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='fixed_data.Building')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='fixed_data.Client')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='LTEInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lteinstallations', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lteinstallations', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MWInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WiMaxInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mwinstallation', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mwpmaintenance', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WiMaxtestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('dbm', models.IntegerField(blank=True, null=True)),
                ('snir', models.IntegerField(blank=True, null=True)),
                ('connecting_bts', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='files/Fixed_data/Winax/')),
                ('router_model', models.IntegerField(blank=True, null=True)),
                ('router_SNMP_CMP_enable', models.BooleanField(default=False)),
                ('power_status', models.BooleanField(default=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wimaxcriteria', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WiMaxPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mwpmaintenamce', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mwpmaintenance', to='fixed_data.WiMaxInstallation')),
                ('test_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mwpmaintenances', to='fixed_data.WiMaxtestCriteria')),
            ],
        ),
        migrations.AddField(
            model_name='wimaxinstallation',
            name='test_criteria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mwinstallations', to='fixed_data.WiMaxtestCriteria'),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('issue', models.CharField(blank=True, max_length=250, null=True)),
                ('resolution', models.CharField(blank=True, max_length=250, null=True)),
                ('fiber_ready', models.BooleanField(default=False)),
                ('remacks', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supports', to='fixed_data.WiMaxInstallation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=150, null=True)),
                ('technology', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='fixed_data.Technology')),
            ],
        ),
        migrations.CreateModel(
            name='MWtestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('dbm', models.IntegerField(blank=True, null=True)),
                ('snir', models.IntegerField(blank=True, null=True)),
                ('connecting_bts', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='files/Fixed_data/Winax/')),
                ('router_model', models.IntegerField(blank=True, null=True)),
                ('router_SNMP_CMP_enable', models.BooleanField(default=False)),
                ('power_status', models.BooleanField(default=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWriterias', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MWPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWmaintenamce', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWmaintenances', to='fixed_data.MWInstallation')),
                ('test_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWmaintenances', to='fixed_data.MWtestCriteria')),
            ],
        ),
        migrations.AddField(
            model_name='mwinstallation',
            name='test_criteria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.MWtestCriteria'),
        ),
        migrations.CreateModel(
            name='LTEtestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('rss_i', models.CharField(blank=True, max_length=250, null=True)),
                ('snir', models.IntegerField(blank=True, null=True)),
                ('snir_capacity', models.IntegerField(blank=True, null=True)),
                ('image', models.FileField(blank=True, help_text='Interface Photo', null=True, upload_to='files/Fixed_data/LTE/')),
                ('router_available', models.IntegerField(blank=True, null=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltecriteria', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LTEPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltemaintenamces', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltemaintenances', to='fixed_data.LTEInstallation')),
                ('test_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltemaintenances', to='fixed_data.LTEtestCriteria')),
            ],
        ),
        migrations.AddField(
            model_name='lteinstallation',
            name='test_criteria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lteinstallations', to='fixed_data.LTEtestCriteria'),
        ),
        migrations.AddField(
            model_name='link',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicelinks', to='fixed_data.Service'),
        ),
        migrations.CreateModel(
            name='FibertestCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('dbm', models.IntegerField(blank=True, null=True)),
                ('snir', models.IntegerField(blank=True, null=True)),
                ('connecting_bts', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='files/Fixed_data/Winax/')),
                ('router_model', models.IntegerField(blank=True, null=True)),
                ('router_SNMP_CMP_enable', models.BooleanField(default=False)),
                ('power_status', models.BooleanField(default=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fibercriterias', to='fixed_data.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberPMaintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fibermaintenances', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fibermaintenance', to='fixed_data.FiberInstallation')),
                ('test_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fibermaintenances', to='fixed_data.FibertestCriteria')),
            ],
        ),
        migrations.AddField(
            model_name='fiberinstallation',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fiberinstallations', to='fixed_data.Link'),
        ),
        migrations.AddField(
            model_name='fiberinstallation',
            name='test_criteria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fiberinstallations', to='fixed_data.FibertestCriteria'),
        ),
        migrations.AddField(
            model_name='consumable',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumables', to='fixed_data.Link'),
        ),
    ]
