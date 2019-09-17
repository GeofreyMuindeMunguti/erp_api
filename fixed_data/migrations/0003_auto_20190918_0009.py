# Generated by Django 2.2.1 on 2019-09-17 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_data', '0002_auto_20190917_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_no',
            field=models.PositiveIntegerField(blank=True, null=True),
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
            name='MWInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.Consumable')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.Link')),
                ('test_criteria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MWinstallations', to='fixed_data.MWtestCriteria')),
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
            options={
                'unique_together': {('link', 'test_criteria')},
            },
        ),
    ]
