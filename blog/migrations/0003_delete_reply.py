# Generated by Django 3.2.10 on 2022-02-02 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]