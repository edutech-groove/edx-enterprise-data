# Generated by Django 1.11.5 on 2018-06-12 05:34


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0006_auto_20180612_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='last_activity_timestamp',
        ),
        migrations.AddField(
            model_name='enterpriseenrollment',
            name='last_activity_date',
            field=models.DateField(null=True),
        ),
    ]
