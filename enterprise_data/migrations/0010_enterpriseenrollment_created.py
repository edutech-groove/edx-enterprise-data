# Generated by Django 1.11.5 on 2018-08-01 18:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0009_auto_20180628_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseenrollment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
