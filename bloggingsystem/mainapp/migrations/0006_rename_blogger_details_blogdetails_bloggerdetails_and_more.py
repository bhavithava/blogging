# Generated by Django 5.0.1 on 2024-03-01 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_blogdetails_blog_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetails',
            old_name='blogger_details',
            new_name='bloggerdetails',
        ),
        migrations.RenameField(
            model_name='blogdetails',
            old_name='blog_title',
            new_name='blogtitle',
        ),
        migrations.RenameField(
            model_name='blogdetails',
            old_name='blog_type',
            new_name='blogtype',
        ),
    ]
