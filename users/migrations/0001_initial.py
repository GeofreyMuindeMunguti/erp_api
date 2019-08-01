# Generated by Django 2.2.1 on 2019-08-01 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_type', models.CharField(max_length=100, unique=True)),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_IP', models.GenericIPAddressField(blank=True, null=True)),
                ('login_datetime', models.DateTimeField(auto_now=True)),
                ('login_username', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, choices=[('S', 'Success'), ('F', 'Failed')], default='S', max_length=1, null=True)),
                ('user_agent_info', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'user_login_activity',
                'verbose_name_plural': 'user_login_activities',
            },
        ),
        migrations.CreateModel(
            name='PermissionMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.BooleanField(default=False)),
                ('edit', models.BooleanField(default=False)),
                ('create', models.BooleanField(default=False)),
                ('approver', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authpermission', to='contenttypes.ContentType')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=100)),
                ('engineer_phone_no', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('eng_profile_pic', models.ImageField(blank=True, null=True, upload_to='ProfilePictures/Engineer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='location', to='users.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engineerprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customuser_phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('customuser_profile_pic', models.ImageField(blank=True, null=True, upload_to='ProfilePictures/Employee')),
                ('team', models.CharField(max_length=150)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Casual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual_name', models.CharField(max_length=150)),
                ('country_code', models.CharField(max_length=100)),
                ('casual_phone_no', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Location')),
            ],
        ),
    ]
