# Generated by Django 4.2.1 on 2023-08-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_alter_projectdetail_groupno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectdetail',
            old_name='div',
            new_name='c_name',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='name',
            new_name='collage',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='groupno',
            new_name='p_year',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='project_detail',
            new_name='s_name',
        ),
        migrations.RenameField(
            model_name='projectdetail',
            old_name='rollno',
            new_name='sem',
        ),
    ]
