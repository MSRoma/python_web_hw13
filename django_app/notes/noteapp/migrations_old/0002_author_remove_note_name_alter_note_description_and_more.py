# Generated by Django 4.2.7 on 2023-12-04 10:38

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
                ('born_date', models.DateTimeField()),
                ('born_location', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='note',
            name='authors',
            field=models.ManyToManyField(to='noteapp.author'),
        ),
    ]