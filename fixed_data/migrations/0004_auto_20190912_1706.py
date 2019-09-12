# Generated by Django 2.2.1 on 2019-09-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_data', '0003_auto_20190912_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/Fixed_data/building/'),
        ),
        migrations.AddField(
            model_name='building',
            name='building_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/Fixed_data/building/'),
        ),
        migrations.AddField(
            model_name='link',
            name='survey_file',
            field=models.FileField(blank=True, null=True, upload_to='files/Fixed_data/surveyfile/'),
        ),
    ]
