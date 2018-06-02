# Generated by Django 2.0.5 on 2018-06-02 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20180602_1749'),
        ('records', '0003_auto_20180602_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(editable=False)),
            ],
        ),
        migrations.RenameField(
            model_name='record',
            old_name='code',
            new_name='source_code',
        ),
        migrations.RemoveField(
            model_name='record',
            name='result_per_test_case',
        ),
        migrations.RemoveField(
            model_name='record',
            name='running_time',
        ),
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.SmallIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testcaseresult',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Record'),
        ),
        migrations.AddField(
            model_name='testcaseresult',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.TestCase'),
        ),
    ]
