# Generated by Django 3.2.7 on 2024-04-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_parking_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('UG', 'Підземна парковка'), ('SM', 'Багатоповерхова парковка'), ('SF', 'Не крита парковка')], max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='status',
            field=models.CharField(choices=[('PF', 'Місце вільне'), ('PR', 'Місце заброньоване'), ('PT', 'Місце зайняте')], default='PF', max_length=2, verbose_name='Статус'),
        ),
    ]