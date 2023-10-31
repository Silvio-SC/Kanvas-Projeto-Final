# Generated by Django 4.2.6 on 2023-10-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='instructor_id',
            new_name='instructor',
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('finished', 'Finished')], default='not started', max_length=20),
        ),
    ]
