# Generated by Django 2.0.6 on 2018-06-13 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malaria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='adhered_to_treament',
            new_name='adhered_to_treatment',
        ),
    ]