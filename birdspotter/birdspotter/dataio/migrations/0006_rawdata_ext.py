# Generated by Django 3.1.6 on 2021-04-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataio', '0005_rawdata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawdata',
            name='ext',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
