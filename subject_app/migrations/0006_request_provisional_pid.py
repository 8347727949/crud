# Generated by Django 4.2.1 on 2023-09-09 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0005_remove_request_provisional_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_provisional',
            name='pid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='subject_app.person'),
        ),
    ]
