# Generated by Django 5.0.4 on 2024-05-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_videoblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/'),
        ),
        migrations.AddField(
            model_name='videoblog',
            name='thubnail',
            field=models.URLField(blank=True, null=True),
        ),
    ]
