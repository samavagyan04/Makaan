# Generated by Django 5.1.6 on 2025-03-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='image')),
                ('text', models.CharField(max_length=255, verbose_name='Some text')),
                ('word1', models.CharField(max_length=255, verbose_name='word1')),
                ('word2', models.CharField(max_length=255, verbose_name='word2')),
                ('word3', models.CharField(max_length=255, verbose_name='word3')),
            ],
        ),
    ]
