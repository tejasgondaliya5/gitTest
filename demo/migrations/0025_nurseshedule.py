# Generated by Django 3.2.3 on 2021-08-31 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0024_delete_nurseshedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurseshedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=None, max_length=50)),
                ('Date', models.DateField()),
                ('Root', models.CharField(choices=[('select', 'select'), ('Morning', 'Morning'), ('Afternoot', 'Afternoot'), ('Evning', 'Evning')], default='', max_length=20)),
                ('Start_time', models.TimeField()),
                ('End_time', models.TimeField()),
            ],
        ),
    ]
