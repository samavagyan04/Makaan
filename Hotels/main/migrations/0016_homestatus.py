# Generated by Django 5.1.6 on 2025-03-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_aboutstatus_delete_clientopinions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=255, verbose_name='text3')),
                ('text4', models.CharField(max_length=255, verbose_name='text4')),
                ('buton_text', models.CharField(max_length=255, verbose_name='buton_text')),
            ],
        ),
    ]
