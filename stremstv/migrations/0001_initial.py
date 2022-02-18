# Generated by Django 4.0.1 on 2022-02-01 08:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xbet_id', models.IntegerField()),
                ('sport', models.CharField(choices=[('Футбол', 'Футбол'), ('Хоккей', 'Хоккей'), ('Биатлон', 'Биатлон'), ('Единоборства', 'Единоборства'), ('UFC', 'UFC'), ('Бокс', 'Бокс'), ('Баскетбол', 'Баскетбол'), ('Формула 1', 'Формула 1'), ('Волейбол', 'Волейбол'), ('Теннис', 'Теннис')], max_length=50)),
                ('country', models.CharField(max_length=150)),
                ('league', models.CharField(max_length=150)),
                ('stage', models.CharField(blank=True, max_length=255, null=True)),
                ('home', models.CharField(max_length=250)),
                ('away', models.CharField(max_length=250)),
                ('start', models.DateTimeField()),
                ('home_logo', models.URLField(blank=True, null=True)),
                ('away_logo', models.URLField(blank=True, null=True)),
                ('score_home', models.IntegerField(blank=True, null=True)),
                ('score_away', models.IntegerField(blank=True, null=True)),
                ('score_periods', models.CharField(blank=True, max_length=255, null=True)),
                ('time_seconds', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('prematch', 'prematch'), ('live', 'live'), ('complete', 'complete')], max_length=25)),
                ('live_status', models.CharField(blank=True, max_length=250, null=True)),
                ('stats', models.JSONField(blank=True, null=True)),
                ('markets', models.JSONField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(choices=[('Жёлтый', 'Жёлтый'), ('Красный', 'Красный'), ('Синий', 'Синий'), ('Random', 'Random')], default='Random', max_length=20)),
                ('stream', models.TextField(blank=True, null=True)),
                ('include', models.BooleanField(default=False)),
                ('update', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=250)),
                ('league', models.CharField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('include', models.BooleanField(default=False)),
                ('exclude', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('sport', 'country', 'league'),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(blank=True, null=True)),
                ('background', models.URLField(blank=True, null=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('reading_time', models.IntegerField(default=8)),
                ('hidden', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
