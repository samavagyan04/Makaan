# Generated by Django 5.1.6 on 2025-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_propertyagent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('imgclient', models.ImageField(upload_to='imgclient', verbose_name='imgclient')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('profession', models.CharField(max_length=255, verbose_name='profession')),
            ],
        ),
    ]
