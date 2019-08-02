# Generated by Django 2.2.1 on 2019-08-02 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_fiber_ftts', '0003_auto_20190802_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manhole',
            old_name='manhole_No',
            new_name='manhole_no',
        ),
        migrations.AddField(
            model_name='fttscivilteam',
            name='ftts_manhole_installation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftts.ManHoleInstallation'),
        ),
        migrations.AlterField(
            model_name='siteinterception',
            name='manhole',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_fiber_ftts.ManHole'),
        ),
    ]
