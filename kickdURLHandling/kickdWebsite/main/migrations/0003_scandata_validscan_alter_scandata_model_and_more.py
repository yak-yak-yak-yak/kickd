# Generated by Django 4.1.7 on 2023-04-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_scandata_tmpr_check_scandata_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scandata',
            name='ValidScan',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scandata',
            name='Model',
            field=models.CharField(default='S', max_length=200),
        ),
        migrations.AlterField(
            model_name='scandata',
            name='TAMP_CHCK',
            field=models.CharField(default='S', max_length=200),
        ),
        migrations.AlterField(
            model_name='scandata',
            name='TKN_ID',
            field=models.CharField(default='S', max_length=200),
        ),
        migrations.AlterField(
            model_name='scandata',
            name='UID',
            field=models.CharField(default='S', max_length=200),
        ),
        migrations.AlterField(
            model_name='scandata',
            name='UTC',
            field=models.CharField(default='S', max_length=200),
        ),
    ]