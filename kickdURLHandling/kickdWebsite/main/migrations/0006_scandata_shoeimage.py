# Generated by Django 4.1.7 on 2023-04-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_scandata_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='scandata',
            name='ShoeImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
