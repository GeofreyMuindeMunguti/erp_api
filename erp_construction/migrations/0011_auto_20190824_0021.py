# Generated by Django 2.2.1 on 2019-08-23 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('erp_construction', '0010_auto_20190824_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlindingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('work_day', models.DateField(blank=True, null=True)),
                ('casuals_list', models.FileField(blank=True, null=True, upload_to='files/bts/Casuals/Blinding/%Y/%m/%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DailyTowerBase',
            new_name='TowerBaseDate',
        ),
        migrations.RemoveField(
            model_name='blindingimage',
            name='project_name',
        ),
        migrations.AlterField(
            model_name='blindingsubtask',
            name='project_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BtsSite'),
        ),
        migrations.DeleteModel(
            name='DailyBlinding',
        ),
        migrations.AddField(
            model_name='blindingdate',
            name='blinding_sub_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BlindingSubTask'),
        ),
        migrations.AddField(
            model_name='blindingdate',
            name='no_of_casuals_atsite',
            field=models.ManyToManyField(blank=True, to='users.Casual'),
        ),
        migrations.AddField(
            model_name='blindingimage',
            name='blinding_date',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_construction.BlindingDate'),
        ),
    ]
