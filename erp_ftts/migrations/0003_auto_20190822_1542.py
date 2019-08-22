# Generated by Django 2.2.1 on 2019-08-22 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('erp_ftts', '0002_auto_20190822_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetrenching',
            name='site_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchings', to='erp_ftts.FttsSite'),
        ),
        migrations.CreateModel(
            name='FTtsDailyCivilWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('distance_trenched', models.FloatField(default=0)),
                ('distance_backfilled', models.FloatField(default=0)),
                ('cable_installed_legth', models.FloatField(default=0)),
                ('poles_installed', models.IntegerField(default=0)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchingsd', to='erp_ftts.FttsSite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_type', models.CharField(choices=[('T', 'Trenching'), ('B', 'Backfilling'), ('CI', 'Cable Installation'), ('TBI', 'ManHole Installation'), ('O', 'Others')], max_length=2)),
                ('site_image_1', models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')),
                ('site_trenching_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchingsfd', to='erp_ftts.FTtsDailyCivilWork')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitetrenchingsfd', to='erp_ftts.FttsSite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
