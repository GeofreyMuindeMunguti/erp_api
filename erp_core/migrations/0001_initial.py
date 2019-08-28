# Generated by Django 2.2.1 on 2019-08-28 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp_ftts', '0001_initial'),
        ('users', '0001_initial'),
        ('erp_ftth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('task_name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.Category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('subtask_name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('task_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('task_name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.Category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberSubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('subtask_name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
                ('task_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_core.FiberTask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberKpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kpi', models.IntegerField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiberBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('beneficiary_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('project_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftth.FTTHProject')),
                ('site_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_ftts.FttsSite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
