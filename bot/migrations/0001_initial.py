# Generated by Django 3.0.8 on 2020-07-30 15:08

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('6', 'sixth'), ('7', 'seventh'), ('8', 'eighth'), ('9', 'ninth'), ('10', 'tenth'), ('11', 'eleventh'), ('12', 'twelfth')], max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Grade',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(choices=[('mt', 'math'), ('sci', 'science'), ('eng', 'english'), ('hin', 'hindi')], max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('answer', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('bot_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade', models.ManyToManyField(to='bot.Grades')),
                ('sub', models.ManyToManyField(to='bot.Subjects')),
            ],
            options={
                'verbose_name_plural': 'questions',
            },
        ),
    ]
