# Generated by Django 2.2.1 on 2019-06-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_construction', '0003_auto_20190616_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementteam',
            name='po_electrical_materials_cost',
            field=models.CharField(blank=True, choices=[('1 - 49kg', '1 - 49kg: 10,000ksh'), ('50 - 99kg', '50 - 99kg: 20,000ksh'), ('100 - 199kg', '100 - 199kg: 30,000ksh'), ('200 - 299kg', '200 - 299kg: 40,000ksh')], default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='procurementteam',
            name='po_subcontractors_cost',
            field=models.CharField(blank=True, choices=[('1 - 49kg', '1 - 49kg: 10,000ksh'), ('50 - 99kg', '50 - 99kg: 20,000ksh'), ('100 - 199kg', '100 - 199kg: 30,000ksh'), ('200 - 299kg', '200 - 299kg: 40,000ksh')], default='None', max_length=120),
        ),
    ]
