# Generated by Django 4.2.4 on 2023-08-13 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raiseticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='owner',
        ),
    ]