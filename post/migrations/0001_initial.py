# Generated by Django 3.2.6 on 2021-08-10 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('attachment', models.FileField(upload_to='posts/attachments/')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Archived')], default=0)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='posts', to='category.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]