# Generated by Django 3.2.7 on 2024-04-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20240421_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_place',
            name='status',
            field=models.CharField(choices=[('PR', 'Місце заброньоване'), ('PT', 'Місце зайняте'), ('PF', 'Місце вільне')], default='PF', max_length=2, verbose_name='Статус'),
        ),
    ]
