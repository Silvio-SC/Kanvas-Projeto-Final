# Generated by Django 4.2.6 on 2023-10-31 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_rename_instructor_id_course_instructor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('finished', 'Finished')], default='not started', max_length=11),
        ),
    ]
