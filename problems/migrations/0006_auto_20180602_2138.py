# Generated by Django 2.0.6 on 2018-06-02 13:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20180602_1754'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='problem',
            managers=[
                ('problem_set', django.db.models.manager.Manager()),
            ],
        ),
    ]
