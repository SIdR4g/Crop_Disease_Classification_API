# Generated by Django 4.1.3 on 2023-08-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CD_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropdiseaseapi',
            name='crop',
            field=models.CharField(max_length=50, null=True),
        ),
    ]