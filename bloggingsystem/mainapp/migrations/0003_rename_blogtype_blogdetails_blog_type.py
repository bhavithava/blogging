# Generated by Django 5.0.1 on 2024-03-01 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_blogdetails_blogtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetails',
            old_name='blogtype',
            new_name='blog_type',
        ),
    ]