# Generated by Django 5.0.6 on 2024-06-04 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_curriculumplan_name_alter_profile_role_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]