# Generated by Django 3.2.3 on 2021-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthymind', '0006_auto_20210529_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeblog',
            name='owner',
            field=models.CharField(max_length=500),
        ),
    ]