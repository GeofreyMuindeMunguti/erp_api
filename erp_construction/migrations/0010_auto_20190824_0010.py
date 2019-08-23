# Generated by Django 2.2.1 on 2019-08-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('erp_construction', '0009_auto_20190823_2351'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailySiteClearing',
            new_name='SiteClearingDate',
        ),
        migrations.AlterField(
            model_name='concretecuringperiodsubtask',
            name='concrete_pour_curing_period_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='concretecuringperiodsubtask',
            name='concrete_pour_curing_period_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='concretecuringperiodsubtask',
            name='concrete_pour_curing_period_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='concretepoursubtask',
            name='concrete_pour_curing_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='concretepoursubtask',
            name='concrete_pour_curing_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='concretepoursubtask',
            name='concrete_pour_curing_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/'),
        ),
    ]
