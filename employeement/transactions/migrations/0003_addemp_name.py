# Generated by Django 3.0.7 on 2022-04-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_addemp'),
    ]

    operations = [
        migrations.AddField(
            model_name='addemp',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
