# Generated by Django 4.1.3 on 2022-12-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
    ]
