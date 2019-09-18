# Generated by Django 2.2.1 on 2019-09-18 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp_ftth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0011_update_proxy_permissions'),
        ('erp_ftts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customuser_phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('customuser_profile_pic', models.ImageField(blank=True, null=True, upload_to='ProfilePictures/Employee')),
                ('team', models.CharField(max_length=150)),
                ('device', models.IntegerField(blank=True, null=True)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host', models.CharField(max_length=1200)),
                ('sender_port', models.IntegerField()),
                ('email_host_user', models.CharField(max_length=1200)),
                ('email_host_password', models.CharField(max_length=1200)),
                ('email_use_ssl', models.BooleanField(default=False)),
                ('email_use_tls', models.BooleanField(default=True)),
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
            ],
        ),
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
            name='TeamMemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='No Subject', max_length=255)),
                ('message', models.CharField(default='No Message', max_length=5000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ProjectTeamFTTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Engineer')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FTTSProject')),
                ('site_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_ftts.FttsSite')),
                ('team_member_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.TeamMemberType')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeamFTTH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Engineer')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_ftth.FTTHProject')),
                ('team_member_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.TeamMemberType')),
            ],
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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='engineer',
            name='location_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='location', to='users.Location'),
        ),
        migrations.AddField(
            model_name='engineer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engineerprofile', to=settings.AUTH_USER_MODEL),
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
