# Generated by Django 5.0.1 on 2024-02-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('blogger_details', models.CharField(max_length=200)),
            ],
        ),
    ]
