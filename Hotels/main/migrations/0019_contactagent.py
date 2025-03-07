# Generated by Django 5.1.6 on 2025-03-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_propertylisting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgagent', models.ImageField(upload_to='imgagent', verbose_name='imgagent')),
                ('ver', models.CharField(max_length=255, verbose_name='ver')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
            ],
        ),
    ]
