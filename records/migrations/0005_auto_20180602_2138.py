# Generated by Django 2.0.6 on 2018-06-02 13:38

from django.db import migrations, models
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20180602_1749'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='record',
            managers=[
                ('record_set', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]