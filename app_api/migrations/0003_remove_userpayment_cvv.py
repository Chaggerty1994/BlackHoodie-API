# Generated by Django 4.0.5 on 2022-06-16 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpayment',
            name='cvv',
        ),
    ]