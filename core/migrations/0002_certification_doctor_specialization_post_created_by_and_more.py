# Generated by Django 5.0.4 on 2024-05-05 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('sessions_count', models.IntegerField(blank=True, default=0, null=True)),
                ('years_of_experience', models.IntegerField(blank=True, default=0, null=True)),
                ('session_price', models.IntegerField(blank=True, default=0, null=True)),
                ('reviews_count', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='core.doctor'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DoctorCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.certification')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specialization')),
            ],
        ),
    ]
