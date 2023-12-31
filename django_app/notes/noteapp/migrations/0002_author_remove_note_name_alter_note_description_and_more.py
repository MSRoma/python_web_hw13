# Generated by Django 5.0 on 2023-12-27 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('born_date', models.CharField(max_length=250)),
                ('born_location', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='noteapp.author'),
        ),
    ]
