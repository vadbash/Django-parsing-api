# Generated by Django 3.2.10 on 2022-10-07 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_rename_notactiveclientslist_noactiveclientslist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientsList',
        ),
        migrations.DeleteModel(
            name='NoActiveClientsList',
        ),
        migrations.DeleteModel(
            name='NotActivePositiveBalance',
        ),
    ]
