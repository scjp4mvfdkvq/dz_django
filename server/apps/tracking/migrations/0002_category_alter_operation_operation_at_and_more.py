
# Generated by Django 5.1.4 on 2024-12-19 11:14


import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 19, 14, 14, 33, 878433), verbose_name='Дата операции'),
        ),
        migrations.AddField(
            model_name='operation',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='tracking.category', verbose_name='Категория операции'),
        ),
    ]
