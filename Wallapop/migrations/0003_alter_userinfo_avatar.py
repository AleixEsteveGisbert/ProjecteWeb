# Generated by Django 4.1.7 on 2023-03-13 21:44

import Wallapop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallapop', '0002_userinfo_alter_ad_id_ad_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(null=True, upload_to=Wallapop.models.user_directory_path),
        ),
    ]
