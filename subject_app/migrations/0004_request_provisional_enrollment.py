# Generated by Django 4.2.1 on 2023-09-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0003_remove_request_provisional_course_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_provisional',
            name='enrollment',
            field=models.IntegerField(default='1'),
        ),
    ]
