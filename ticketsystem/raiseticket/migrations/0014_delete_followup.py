# Generated by Django 4.2.4 on 2023-08-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raiseticket', '0013_remove_customer_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowUp',
        ),
    ]
