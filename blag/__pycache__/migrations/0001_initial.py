# Generated by Django 4.1.6 on 2023-02-06 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('puplish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]
