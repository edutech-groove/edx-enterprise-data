# Generated by Django 1.11.15 on 2019-03-29 12:41


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0020_add_role_based_access_control_switch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprisedataroleassignment',
            name='role',
        ),
        migrations.RemoveField(
            model_name='enterprisedataroleassignment',
            name='user',
        ),
        migrations.DeleteModel(
            name='EnterpriseDataFeatureRole',
        ),
        migrations.DeleteModel(
            name='EnterpriseDataRoleAssignment',
        ),
    ]
