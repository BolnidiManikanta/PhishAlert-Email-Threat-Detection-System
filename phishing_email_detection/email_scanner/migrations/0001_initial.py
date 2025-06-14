# Generated by Django 5.1 on 2024-09-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailScanResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('from_email', models.EmailField(max_length=254)),
                ('header_analysis', models.JSONField()),
                ('attachment_scan_results', models.JSONField()),
                ('links_scan_results', models.JSONField()),
                ('scan_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
