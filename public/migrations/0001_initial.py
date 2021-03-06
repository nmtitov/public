# Generated by Django 2.2.2 on 2019-06-10 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=128, unique=True)),
                ('verbose_title', models.CharField(max_length=1024)),
                ('priority', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=1024)),
                ('footer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('internal_title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('thumbnail', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('sidebar', models.TextField(blank=True)),
                ('hidden', models.BooleanField(db_index=True, default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='public.Section')),
            ],
        ),
    ]
