# Generated by Django 4.2.6 on 2023-10-25 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), (' finished', 'Finished')], default='not started', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
