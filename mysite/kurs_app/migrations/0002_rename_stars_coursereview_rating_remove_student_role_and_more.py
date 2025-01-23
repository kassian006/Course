# Generated by Django 5.1.5 on 2025-01-22 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursereview',
            old_name='stars',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='student',
            name='role',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')], default='student', max_length=16),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_certificate', to='kurs_app.course'),
        ),
    ]
