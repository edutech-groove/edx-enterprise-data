# Generated by Django 1.11.15 on 2018-09-24 21:38


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0015_auto_20180907_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='consent_granted',
            field=models.NullBooleanField(default=None),
        ),
    ]
