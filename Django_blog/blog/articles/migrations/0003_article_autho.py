# Generated by Django 3.1.3 on 2021-01-02 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201231_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='autho',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
