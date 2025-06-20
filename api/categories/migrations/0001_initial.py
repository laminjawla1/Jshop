# Generated by Django 5.2.3 on 2025-06-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
    ]
