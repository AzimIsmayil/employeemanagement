# Generated by Django 3.0.7 on 2022-04-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_addemp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='addemp',
            name='designation',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='addemp',
            name='salary',
            field=models.CharField(max_length=40, null=True),
        ),
    ]