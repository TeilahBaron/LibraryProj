# Generated by Django 5.0.7 on 2024-07-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libs_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='reader_contac',
            new_name='reader_contact',
        ),
    ]
