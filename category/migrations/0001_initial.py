# Generated by Django 3.2.6 on 2021-08-10 18:42

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
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
