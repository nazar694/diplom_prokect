# Generated by Django 4.2.11 on 2024-04-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_rename_phone_account_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalparking_place',
            name='status',
            field=models.CharField(choices=[('PF', 'Місце вільне'), ('PT', 'Місце зайняте'), ('PR', 'Місце заброньоване')], default='PF', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='parking_place',
            name='status',
            field=models.CharField(choices=[('PF', 'Місце вільне'), ('PT', 'Місце зайняте'), ('PR', 'Місце заброньоване')], default='PF', max_length=2, verbose_name='Статус'),
        ),
    ]
