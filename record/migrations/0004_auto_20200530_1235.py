# Generated by Django 3.0.6 on 2020-05-30 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20200528_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(upload_to='record/2020/05/30'),
        ),
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
