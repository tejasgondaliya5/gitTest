# Generated by Django 3.2.3 on 2021-08-31 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0027_auto_20210831_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Book_name',
        ),
        migrations.AlterField(
            model_name='cart',
            name='joinuser',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo.userdetail'),
        ),
    ]
