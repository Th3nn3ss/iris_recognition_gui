# Generated by Django 3.2.6 on 2021-08-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0004_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], default=2, max_length=10),
        ),
    ]
